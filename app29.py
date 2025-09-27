
"""
This module provides a Flask-based API for calculating Indian income tax
under both the old and new regimes. It has been rebuilt to use a direct
REST API call to the Gemini API for enhanced stability and control.
"""

import json
import os
import re
from typing import Dict, Any, List, Tuple

import requests
from flask import Flask, request, jsonify, Response

# --- Configuration ---
# All tax rules, slabs, and limits are defined here for easy updates.
TAX_CONFIG: Dict[str, Any] = {
    'cess_rate': 0.04,
    'deductions': {
        '80c_max': 150000
    },
    'old_regime': {
        'standard_deduction': 50000, # Correct standard deduction for Old Regime
        'slabs': [
            {'limit': 250000, 'rate': 0.0},
            {'limit': 500000, 'rate': 0.05},
            {'limit': 1000000, 'rate': 0.20},
            {'limit': float('inf'), 'rate': 0.30}
        ],
        'rebate': {
            'taxable_income_limit': 500000,
            'max_rebate': 12500
        }
    },
    'new_regime': {
        'standard_deduction': 75000, # Correct standard deduction for New Regime
        'slabs': [
            {'limit': 300000, 'rate': 0.0},
            {'limit': 600000, 'rate': 0.05},
            {'limit': 900000, 'rate': 0.10},
            {'limit': 1200000, 'rate': 0.15},
            {'limit': 1500000, 'rate': 0.20},
            {'limit': float('inf'), 'rate': 0.30}
        ],
        'rebate': {
            'taxable_income_limit': 700000,
            'max_rebate': 25000
        }
    }
}


# --- Gemini API Integration Service (REST Implementation) ---
class GeminiService:
    """A service to handle all interactions with the Gemini API via REST."""
    def __init__(self, api_key: str):
        """
        Initializes the service with the API key and endpoint.
        Args:
            api_key: The Gemini API key.
        """
        self.api_key = api_key
        self.api_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-pro:generateContent"
        self.system_prompt = (
            "You are an expert-level Indian tax professional acting as a fiduciary financial advisor. Your primary directive is to provide accurate, actionable, and legally sound tax-saving suggestions based on the user's financial data. "
            "Your advice must be rigorously based on the Indian Income Tax Act, 1961, and relevant Finance Acts for the current assessment year. "
            "CRITICAL: You MUST use the integrated Google Search tool to ground every single claim and suggestion you make. Advice not supported by verifiable, real-world sources is unacceptable. "
            "For each suggestion, you must cite the specific section of the Income Tax Act (e.g., 'Section 80D', 'Section 24(b)'). "
            "Focus on common deductions beyond Section 80C, such as Section 80D (health insurance), Section 24b (home loan interest), and NPS contributions. Do not suggest anything related to Section 80C, as it is already handled. "
            "Your entire response must be a single, valid JSON array of objects, and nothing else. Do not wrap it in markdown backticks. Each object must contain the following keys: 'section', 'suggestion', 'potential_tax_saving', and 'reasoning'. "
            "The 'reasoning' field must explain how the financial data makes the user eligible under the cited tax law section and why it's a sound financial strategy for them, referencing the information you found via search."
        )

    def get_suggestions(self, financial_summary: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
        """
        Fetches personalized tax-saving suggestions from the Gemini API using a direct REST call.
        Args:
            financial_summary: A dictionary containing the user's financial data.
        Returns:
            A tuple containing a list of suggestions and a list of sources.
        """
        user_prompt = (
            "Based on the following financial data, please provide 1-2 actionable tax-saving suggestions for me in the specified JSON format. Ensure every suggestion is grounded using the search tool and cites the relevant tax law. "
            f"Financial Summary:\n{json.dumps(financial_summary, indent=2)}"
        )
        suggestions = []
        sources: List[Dict[str, Any]] = []

        headers = {
            'x-goog-api-key': self.api_key,
            'Content-Type': 'application/json'
        }
        
        payload = {
            "contents": [{"parts": [{"text": user_prompt}]}],
            "tools": [{"google_search": {}}],
            "systemInstruction": {"parts": [{"text": self.system_prompt}]}
        }

        try:
            response = requests.post(self.api_url, headers=headers, json=payload, timeout=60)
            response.raise_for_status()  # Will raise an HTTPError for bad responses (4xx or 5xx)
            
            response_data = response.json()

            # --- Robust Response Handling ---
            if not response_data.get('candidates'):
                print("Warning: Gemini API response did not contain 'candidates'.")
                return [], []
            
            candidate = response_data['candidates'][0]
            suggestions_text = candidate.get('content', {}).get('parts', [{}])[0].get('text', '').strip()
            
            if not suggestions_text:
                print("Warning: Gemini API returned an empty text response.")
                return [], []

            # Clean markdown fences from the response string.
            if suggestions_text.startswith("```json"):
                suggestions_text = suggestions_text[7:]
            if suggestions_text.endswith("```"):
                suggestions_text = suggestions_text[:-3]
            suggestions_text = suggestions_text.strip()

            try:
                parsed_suggestions = json.loads(suggestions_text)
                if isinstance(parsed_suggestions, list) and all(isinstance(item, dict) for item in parsed_suggestions):
                    suggestions = parsed_suggestions
                else:
                    print(f"Warning: API response was valid JSON but not a list of objects. Response: {suggestions_text}")
            except json.JSONDecodeError:
                print(f"Error: Failed to decode JSON from API response. Text: {suggestions_text}")

            # Extract citation sources from grounding metadata
            grounding_meta = candidate.get('groundingMetadata', {})
            if grounding_meta and 'groundingChunks' in grounding_meta:
                for chunk in grounding_meta['groundingChunks']:
                    if 'web' in chunk and chunk['web'].get('uri'):
                        sources.append({
                            "title": chunk['web'].get('title', 'N/A'),
                            "url": chunk['web']['uri']
                        })

        except requests.exceptions.RequestException as e:
            print(f"An error occurred during the REST API call: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            
        return suggestions, sources

# --- Core Calculation Logic (Unchanged) ---
def calculate_tax_from_slabs(income: float, slabs: List[Dict[str, float]]) -> float:
    tax = 0.0; previous_limit = 0.0
    for slab in slabs:
        if income > previous_limit:
            taxable_in_slab = min(income - previous_limit, slab['limit'] - previous_limit)
            tax += taxable_in_slab * slab['rate']
            previous_limit = slab['limit']
        else: break
    return tax

def get_marginal_rate(income: float, slabs: List[Dict[str, float]]) -> float:
    previous_limit = 0.0
    for slab in slabs:
        if previous_limit < income <= slab['limit']: return slab['rate']
        previous_limit = slab['limit']
    return slabs[-1]['rate'] if slabs else 0.0

def compute_tax_for_regime(taxable_income: float, regime_config: Dict[str, Any]) -> float:
    tax_before_rebate = calculate_tax_from_slabs(taxable_income, regime_config['slabs'])
    rebate = 0.0
    rebate_config = regime_config['rebate']
    if taxable_income <= rebate_config['taxable_income_limit']:
        rebate = min(tax_before_rebate, rebate_config['max_rebate'])
    tax_after_rebate = tax_before_rebate - rebate
    cess = tax_after_rebate * TAX_CONFIG['cess_rate']
    return tax_after_rebate + cess

# --- Helper Function for Robust Parsing ---
def parse_saving_amount(value: Any) -> float:
    """
    Intelligently parses a numeric value from various input types.
    Handles integers, floats, and strings containing numbers.
    """
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        numbers = re.findall(r'[\d,]+', value)
        if numbers:
            try:
                return float(numbers[0].replace(',', ''))
            except (ValueError, IndexError):
                return 0.0
    return 0.0

# --- Main Service Logic ---
def get_tax_analysis(user_data: Dict[str, Any], gemini_service: GeminiService | None) -> Tuple[Dict[str, Any], int]:
    try:
        session_id = user_data['session_id']
        tax_data = user_data['tax_relevant_data']
        annual_income = tax_data['estimated_annual_income']
        monthly_income = tax_data['monthly_salary']
        investments = tax_data['tax_saving_investments']
        total_deductions = investments['total_deductions']
        c80_investments = investments['80c_investments']
    except KeyError as e:
        return {"error": f"Missing required key in input data: {e}"}, 400

    # CORRECTED LOGIC: Pull the correct standard deduction for each regime
    std_deduction_old = TAX_CONFIG['old_regime']['standard_deduction']
    std_deduction_new = TAX_CONFIG['new_regime']['standard_deduction']

    taxable_old = max(0, annual_income - std_deduction_old - total_deductions)
    total_tax_old = compute_tax_for_regime(taxable_old, TAX_CONFIG['old_regime'])

    taxable_new = max(0, annual_income - std_deduction_new)
    total_tax_new = compute_tax_for_regime(taxable_new, TAX_CONFIG['new_regime'])

    effective_old = round(total_tax_old / annual_income * 100, 2) if annual_income > 0 else 0
    effective_new = round(total_tax_new / annual_income * 100, 2) if annual_income > 0 else 0

    if total_tax_old < total_tax_new:
        recommended_regime, savings = "Old Regime", total_tax_new - total_tax_old
    else:
        recommended_regime, savings = "New Regime", total_tax_old - total_tax_old
        
    all_suggestions, gemini_sources = [], []
    max_80c = TAX_CONFIG['deductions']['80c_max']
    additional_80c_needed = max(0, max_80c - c80_investments)
    if additional_80c_needed > 0 and recommended_regime == "Old Regime":
        marginal_rate = get_marginal_rate(taxable_old, TAX_CONFIG['old_regime']['slabs'])
        potential_saving = round(additional_80c_needed * marginal_rate * (1 + TAX_CONFIG['cess_rate']))
        all_suggestions.append({
            "section": "80C", "suggestion": f"Invest additional ₹{additional_80c_needed:,.0f} in ELSS/PPF",
            "potential_tax_saving": potential_saving, "investment_options": ["ELSS Mutual Funds", "PPF", "EPF"]})
    
    if gemini_service:
        summary_for_ai = {k: v for k, v in locals().items() if k in ["annual_income", "c80_investments", "total_deductions", "recommended_regime"]}
        gemini_suggestions, gemini_sources = gemini_service.get_suggestions(summary_for_ai)
        all_suggestions.extend(gemini_suggestions)
    
    output = {
        "session_id": session_id,
        "income_analysis": {"annual_income": int(annual_income), "monthly_income": int(monthly_income), "current_deductions": int(total_deductions)},
        "tax_calculation": {
            "old_regime": {"total_tax": int(round(total_tax_old)), "effective_tax_rate": effective_old, "taxable_income": int(taxable_old)},
            "new_regime": {"total_tax": int(round(total_tax_new)), "effective_tax_rate": effective_new, "taxable_income": int(taxable_new)},
            "recommended_regime": recommended_regime, "savings": int(round(savings))},
        "deduction_optimization": {
            "optimization_suggestions": all_suggestions,
            "total_potential_savings": int(round(sum(parse_saving_amount(s.get('potential_tax_saving', 0)) for s in all_suggestions))),
            "sources": gemini_sources}}
    return output, 200

# --- API Endpoint ---
app = Flask(__name__)
api_key = os.environ.get("GEMINI_API_KEY")
gemini_service_instance = GeminiService(api_key) if api_key else None
if gemini_service_instance: print("--- Gemini Service Initialized (REST) ---")
else: print("--- Warning: GEMINI_API_KEY not found. AI suggestions disabled. ---")

@app.route('/analyze-tax', methods=['POST'])
def analyze_tax_endpoint() -> Response:
    user_data = request.get_json()
    if not user_data: return jsonify({"error": "Invalid JSON in request body"}), 400
    result, status_code = get_tax_analysis(user_data, gemini_service_instance)
    return jsonify(result), status_code

if __name__ == '__main__':
    print("--- Starting Flask Server ---")
    app.run(debug=True, host='0.0.0.0', port=5000)

