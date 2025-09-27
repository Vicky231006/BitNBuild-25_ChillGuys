
"""
This module provides a Flask-based API for calculating Indian income tax
under both the old and new regimes. It has been rebuilt to use a direct
REST API call to the Gemini API for enhanced stability and control.
"""

import json
import os
import re
import time
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
            "You are a forensic tax analyst and optimization expert. Your primary goal is to be maximally aggressive in finding tax-saving opportunities for the user by meticulously analyzing their raw transaction data. "
            "Your advice must be rigorously based on the Indian Income Tax Act, 1961. "
            "CRITICAL DIRECTIVES: "
            "1. **Forensic Transaction Analysis:** Scan every single transaction description in 'income_transactions', 'investment_transactions', and 'deduction_eligible_expenses'. Your task is to find hidden clues. For example: "
            "   - A transaction like 'Payment to Max Life Insurance' is a potential Section 80D (health) or 80C (life) deduction. "
            "   - 'EMI - HDFC Bank' could be a home loan; you must suggest verifying this for a Section 24(b) deduction. "
            "   - 'Donation - GiveIndia' is a clear flag for a Section 80G deduction. "
            "   - 'School Fee' transactions are potential Section 80C deductions for tuition fees. "
            "2. **MANDATORY Grounding and Citation:** This is your most important directive. "
            "   a. **Use Google Search:** You MUST use the integrated Google Search tool to verify every piece of tax advice. Do not answer from memory. "
            "   b. **Cite Grounded URLs Directly:** The `sources` array for each suggestion MUST contain the direct, uncleaned URLs provided by the Google Search tool. These URLs will contain 'vertexaisearch.cloud.google.com'. Do not resolve these to the final destination URL; use the raw link provided by the search grounding process. "
            "   c. **Link Reasoning to Sources:** Your `reasoning` text for each suggestion must be directly derived from the information present in the sources you cite. "
            "3. **Justify with Data:** For each suggestion, your 'reasoning' MUST explicitly reference the transaction description(s) that triggered your analysis (e.g., 'Based on your transaction described as \"LIC Premium Payment\", you may be eligible...'). "
            "4. **Strict JSON Output:** Your entire response MUST be a single, valid JSON array of objects. Do not wrap it in markdown. Each object must contain these keys: "
            "   - 'section': The specific section of the Income Tax Act (e.g., 'Section 80D'). "
            "   - 'suggestion': A clear, actionable suggestion for the user. "
            "   - 'potential_tax_saving': A quantified estimate of the potential tax saving. "
            "   - 'reasoning': The detailed explanation, referencing specific transactions and supported by your cited sources. "
            "   - 'sources': A JSON array of source objects, where each object has 'title' and 'url' keys, providing the verifiable, raw, grounded URLs for this specific suggestion."
        )

    def get_suggestions(self, financial_summary: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Fetches personalized tax-saving suggestions from the Gemini API using a direct REST call.
        Now expects sources to be nested within each suggestion.
        Args:
            financial_summary: A dictionary containing the user's detailed financial data.
        Returns:
            A list of suggestion dictionaries, each potentially containing its own list of sources.
        """
        user_prompt = (
            "Based on the following comprehensive financial data, please provide all actionable tax-saving suggestions you can find for me in the specified JSON format. "
            "Analyze the transaction lists carefully for hidden opportunities. Ensure every suggestion is grounded, cites the relevant tax law, and includes its own list of sources. "
            f"Financial Summary:\n{json.dumps(financial_summary, indent=2)}"
        )
        suggestions = []

        headers = {
            'x-goog-api-key': self.api_key,
            'Content-Type': 'application/json'
        }
        
        payload = {
            "contents": [{"parts": [{"text": user_prompt}]}],
            "tools": [{"google_search": {}}],
            "systemInstruction": {"parts": [{"text": self.system_prompt}]}
        }

        # --- Retry Logic with Exponential Backoff ---
        max_retries = 3
        base_delay = 1  # seconds
        for attempt in range(max_retries):
            try:
                # Increased timeout to 180 seconds (3 minutes) to allow for complex processing
                response = requests.post(self.api_url, headers=headers, json=payload, timeout=180)

                # If the status code is a server error (5xx), retry
                if 500 <= response.status_code < 600:
                    print(f"Warning: Received server error {response.status_code}. Retrying in {base_delay * (2 ** attempt)}s...")
                    time.sleep(base_delay * (2 ** attempt))
                    continue # Go to the next attempt

                response.raise_for_status() # Raise an exception for other bad status codes (4xx)
                
                response_data = response.json()

                if not response_data.get('candidates'):
                    print("Warning: Gemini API response did not contain 'candidates'.")
                    return []
                
                candidate = response_data['candidates'][0]
                suggestions_text = candidate.get('content', {}).get('parts', [{}])[0].get('text', '').strip()
                
                if not suggestions_text:
                    print("Warning: Gemini API returned an empty text response.")
                    return []

                if suggestions_text.startswith("```json"):
                    suggestions_text = suggestions_text[7:]
                if suggestions_text.endswith("```"):
                    suggestions_text = suggestions_text[:-3]
                suggestions_text = suggestions_text.strip()

                try:
                    parsed_suggestions = json.loads(suggestions_text)
                    if isinstance(parsed_suggestions, list) and all(isinstance(item, dict) for item in parsed_suggestions):
                        return parsed_suggestions # Success, exit the loop and return
                    else:
                        print(f"Warning: API response was valid JSON but not a list of objects. Response: {suggestions_text}")
                        return [] # Not a retryable error
                except json.JSONDecodeError:
                    print(f"Error: Failed to decode JSON from API response. Text: {suggestions_text}")
                    return [] # Not a retryable error

            except requests.exceptions.RequestException as e:
                print(f"An error occurred during the REST API call: {e}")
                if attempt < max_retries - 1:
                    time.sleep(base_delay * (2 ** attempt))
                else:
                    break # Max retries reached
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                break # Non-retryable error, exit the loop
        
        return suggestions # Return empty list if all retries fail


# --- Core Calculation Logic ---
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
        annual_income = tax_data['estimated_annual_income'] + tax_data.get('other_income', 0)
        monthly_income = tax_data['monthly_salary']
        investments = tax_data['tax_saving_investments']
        total_deductions = investments['total_deductions']
        c80_investments = investments['80c_investments']
    except KeyError as e:
        return {"error": f"Missing required key in input data: {e}"}, 400

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
        recommended_regime, savings = "New Regime", total_tax_old - total_tax_new
        
    all_suggestions = []
    max_80c = TAX_CONFIG['deductions']['80c_max']
    additional_80c_needed = max(0, max_80c - c80_investments)
    if additional_80c_needed > 0 and recommended_regime == "Old Regime":
        marginal_rate = get_marginal_rate(taxable_old, TAX_CONFIG['old_regime']['slabs'])
        potential_saving = round(additional_80c_needed * marginal_rate * (1 + TAX_CONFIG['cess_rate']))
        all_suggestions.append({
            "section": "80C", "suggestion": f"Invest additional ₹{additional_80c_needed:,.0f} in ELSS/PPF",
            "potential_tax_saving": potential_saving, "investment_options": ["ELSS Mutual Funds", "PPF", "EPF"], "sources": []})
    
    if gemini_service:
        # Pass the full, detailed user data to the AI for deep analysis
        summary_for_ai = {
            "tax_relevant_data": tax_data,
            "income_transactions": user_data.get("income_transactions", []),
            "investment_transactions": user_data.get("investment_transactions", []),
            "deduction_eligible_expenses": user_data.get("deduction_eligible_expenses", []),
            "calculated_recommendation": recommended_regime
        }
        gemini_suggestions = gemini_service.get_suggestions(summary_for_ai)
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
            "total_potential_savings": int(round(sum(parse_saving_amount(s.get('potential_tax_saving', 0)) for s in all_suggestions)))
        } # Removed top-level 'sources' key
    }
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
