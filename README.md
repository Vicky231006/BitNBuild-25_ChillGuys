
### Output: 
```
{
  "session_id": "8153ea55-b336-4b2c-9bf5-d7ab93fccd01",
  "timestamp": "2025-09-27T...",
  "cibil_score": 801,
  "status": "Excellent",
  "components": {
    "payment_history": 95.4,
    "credit_utilization": 87.0,
    "credit_mix": 85.0,
    "debt_to_income": 70.0,
    "credit_inquiries": 80.0
  },
  "metrics": {
    "utilization_pct": "33%",
    "dti_pct": "49%",
    "monthly_emi": "₹29,350",
    "credit_types": 5
  },
  "advice": [
    "Reduce credit utilization below 30%",
    "Maintain consistent payment history"
  ],
  "chart_base64": "iVBORw0KGgoAAAANSUhEUgAA..." // Base64 chart image
}
```

# Meaning

# Analysis Session Data

**session_id** (String): Unique identifier for the user's analysis session.
* **timestamp** (String): Date and time when the analysis was generated.

## CIBIL Score
* **cibil_score** (Integer): Estimated CIBIL score (300-900). A higher score indicates better creditworthiness.
* **status** (String): Qualitative assessment of the score (e.g., "Excellent", "Good", "Poor").

## CIBIL Score Components
* **components** (Object):
  * **payment_history** (Float): Score for on-time payment behavior (35% weight).
  * **credit_utilization** (Float): Score based on Credit Utilization Ratio (30% weight).
  * **credit_mix** (Float): Score reflecting variety of credit accounts (10% weight).
  * **debt_to_income** (Float): Score based on Debt-to-Income Ratio (15% weight).
  * **credit_inquiries** (Float): Score based on recent hard inquiries (10% weight).

## Key Performance Indicators (KPIs)
* **metrics** (Object):
  * **utilization_pct** (String): Calculated Credit Utilization Ratio (e.g., 33%). Ideal is below 30%.
  * **dti_pct** (String): Calculated Debt-to-Income Ratio (e.g., 49%). Ideal is below 30-40%.
  * **monthly_emi** (String): Total estimated monthly debt burden (Equated Monthly Installment).
  * **credit_types** (Integer): Count of different loan/credit types contributing to Credit Mix.

## Personalized Recommendations
* **advice** (Array): Recommendations to improve CIBIL score based on analysis.

## Data Visualization
* **chart_base64** (String): Base64 encoded string representing an image (e.g., chart or graph) of analysis data.
