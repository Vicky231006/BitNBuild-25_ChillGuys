# TAX Calculator Module 
## Index:
[Installation](https://github.com/Vicky231006/BitNBuild-25_ChillGuys/blob/Ashutosh/README.md#instructions-to-use)    
[Input](https://github.com/Vicky231006/BitNBuild-25_ChillGuys/blob/Ashutosh/README.md#Input)  
[Output](https://github.com/Vicky231006/BitNBuild-25_ChillGuys/blob/Ashutosh/README.md#Output)  
## Instructions to Use:
Git Clone the repo and Cd into it.
### Step 1: 
`pip install -r requirements.txt`
### Step 2: 
`Export GEMINI_API_KEY="ENTER VALUE HERE"`
### Step 3:
`Python3 app39.py`
### Step 4:
Make a REST POST API request. Look at the sample Input for examples.

## Input:

### Run Curl command with input stored in file input.json and output in output.json : 

`curl -X POST http://127.0.0.1:5000/analyze-tax -H "Content-Type: application/json" -d '@input.json' > output.json`


### Input.json:
```
{
  "session_id": "6237d0b9-7bbb-4210-b622-862a9709d2b8",
  "tax_relevant_data": {
    "estimated_annual_income": 9360000,
    "monthly_salary": 780000,
    "tax_saving_investments": {
      "80c_investments": 120000,
      "insurance_premiums": 0,
      "total_deductions": 120000
    },
    "investment_categories": {
      "Tax_Saving": 96000,
      "PF_PPF": 24000
    },
    "other_income": 174699
  },
  "income_analysis": {
    "total_income": 954699,
    "monthly_average": 954699,
    "income_stability": 0
  },
  "income_transactions": [
    {
      "id": "89f8a67e-c263-4423-b0d4-5755f91e6fe7",
      "date": "2025-09-27",
      "description": "Salary Credit - TCS Ltd",
      "amount": 60000,
      "category": "Income",
      "type": "income",
      "subcategory": "Salary",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.95
    },
    {
      "id": "5df00d68-f5fa-4ec5-ae48-4c99bc778849",
      "date": "2025-09-27",
      "description": "Salary Credit - TCS Ltd",
      "amount": 60000,
      "category": "Income",
      "type": "income",
      "subcategory": "Salary",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.95
    },
    {
      "id": "8f94d487-cd07-4704-a5df-6830c23f46ed",
      "date": "2025-09-27",
      "description": "Salary Credit - TCS Ltd",
      "amount": 60000,
      "category": "Income",
      "type": "income",
      "subcategory": "Salary",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.95
    },
    {
      "id": "e3928acc-89b4-4de8-8e4a-b89d65b0f648",
      "date": "2025-09-27",
      "description": "Entertainment - PVR Cinemas",
      "amount": 800,
      "category": "Other_Income",
      "type": "income",
      "subcategory": "Miscellaneous",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.3
    },
    {
      "id": "5616e936-6295-4652-9939-f6279ec81ea1",
      "date": "2025-09-27",
      "description": "Salary Credit - TCS Ltd",
      "amount": 60000,
      "category": "Income",
      "type": "income",
      "subcategory": "Salary",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.95
    },
    {
      "id": "8111a445-b1dd-4020-ae6c-73c8a31b1a04",
      "date": "2025-09-27",
      "description": "Shopping - Amazon",
      "amount": 2800,
      "category": "Other_Income",
      "type": "income",
      "subcategory": "Miscellaneous",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.3
    },
    {
      "id": "94fe9a69-a8ab-4fe9-b400-efa2a4909bd1",
      "date": "2025-09-27",
      "description": "Salary Credit - TCS Ltd",
      "amount": 60000,
      "category": "Income",
      "type": "income",
      "subcategory": "Salary",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.95
    },
    {
      "id": "e223de0f-74fe-4ab5-9860-b6dc06df2eec",
      "date": "2025-09-27",
      "description": "Salary Credit - TCS Ltd",
      "amount": 60000,
      "category": "Income",
      "type": "income",
      "subcategory": "Salary",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.95
    },
    {
      "id": "105429b4-beea-4795-9637-ac8db04c9ddc",
      "date": "2025-09-27",
      "description": "Dining - McDonald's",
      "amount": 900,
      "category": "Other_Income",
      "type": "income",
      "subcategory": "Miscellaneous",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.3
    },
    {
      "id": "66dac2f0-02d6-4a78-a34a-b469702562c5",
      "date": "2025-09-27",
      "description": "Salary Credit - TCS Ltd",
      "amount": 60000,
      "category": "Income",
      "type": "income",
      "subcategory": "Salary",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.95
    },
    {
      "id": "37038b2c-086a-42c8-9bc2-13d7ff937998",
      "date": "2025-09-27",
      "description": "Entertainment - BookMyShow",
      "amount": 1200,
      "category": "Other_Income",
      "type": "income",
      "subcategory": "Miscellaneous",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.3
    },
    {
      "id": "1e2f84b1-7e09-44a2-8fbf-c85091c70fa9",
      "date": "2025-09-27",
      "description": "Salary Credit - TCS Ltd",
      "amount": 60000,
      "category": "Income",
      "type": "income",
      "subcategory": "Salary",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.95
    },
    {
      "id": "07a6f577-dbf4-469a-aa70-fabf5a06e029",
      "date": "2025-09-27",
      "description": "Shopping - Myntra",
      "amount": 2200,
      "category": "Other_Income",
      "type": "income",
      "subcategory": "Miscellaneous",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.3
    },
    {
      "id": "99515853-c879-41ed-a34b-ec70a2c440c0",
      "date": "2025-09-27",
      "description": "Salary Credit - TCS Ltd",
      "amount": 60000,
      "category": "Income",
      "type": "income",
      "subcategory": "Salary",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.95
    },
    {
      "id": "cf75862e-86e7-4427-bca7-46616a21b138",
      "date": "2025-09-27",
      "description": "Salary Credit - TCS Ltd",
      "amount": 60000,
      "category": "Income",
      "type": "income",
      "subcategory": "Salary",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.95
    },
    {
      "id": "85f923f3-34d1-47cb-be07-1b807085d1c8",
      "date": "2025-09-27",
      "description": "Salary Credit - TCS Ltd",
      "amount": 60000,
      "category": "Income",
      "type": "income",
      "subcategory": "Salary",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.95
    },
    {
      "id": "d70ab1e3-1945-4285-a329-e09e4a21e4e2",
      "date": "2025-09-27",
      "description": "Entertainment - Wonderla",
      "amount": 1800,
      "category": "Other_Income",
      "type": "income",
      "subcategory": "Miscellaneous",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.3
    },
    {
      "id": "653d2b0f-9f25-4288-a096-5caacaa2ed2c",
      "date": "2025-09-27",
      "description": "Salary Credit - TCS Ltd",
      "amount": 60000,
      "category": "Income",
      "type": "income",
      "subcategory": "Salary",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.95
    },
    {
      "id": "fbe49f2b-c631-4d5c-b16d-807b0d9d7697",
      "date": "2025-09-27",
      "description": "Shopping - Flipkart",
      "amount": 3200,
      "category": "Other_Income",
      "type": "income",
      "subcategory": "Miscellaneous",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.3
    },
    {
      "id": "d5edf9d1-185a-4bf0-9c29-d577b69aca6b",
      "date": "2025-09-27",
      "description": "Dining - Domino's",
      "amount": 1100,
      "category": "Other_Income",
      "type": "income",
      "subcategory": "Miscellaneous",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.3
    },
    {
      "id": "a9135ef5-fc91-460f-b0d4-836a75191093",
      "date": "2025-09-27",
      "description": "Year End Bonus",
      "amount": 10000,
      "category": "Income",
      "type": "income",
      "subcategory": "Bonus",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.9
    },
    {
      "id": "cbd09ab6-3e0a-47b0-9963-b0302041cb0e",
      "date": "2025-09-27",
      "description": "ATM Cash Withdrawal",
      "amount": 5000,
      "category": "Other_Income",
      "type": "income",
      "subcategory": "Miscellaneous",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.3
    },
    {
      "id": "20998a53-36c3-4468-8960-d15ff8a78c57",
      "date": "2025-09-27",
      "description": "Valentine's Day Shopping",
      "amount": 2500,
      "category": "Other_Income",
      "type": "income",
      "subcategory": "Miscellaneous",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.3
    },
    {
      "id": "331bff97-d565-4d0a-9457-e3c12786dc8d",
      "date": "2025-09-27",
      "description": "Women's Day Gift",
      "amount": 1200,
      "category": "Other_Income",
      "type": "income",
      "subcategory": "Miscellaneous",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.3
    },
    {
      "id": "bf2763e8-ce51-482e-b461-88dadbdc92fb",
      "date": "2025-09-27",
      "description": "Friend's Wedding Gift",
      "amount": 5000,
      "category": "Other_Income",
      "type": "income",
      "subcategory": "Miscellaneous",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.3
    },
    {
      "id": "68458840-843b-4109-9fb7-4fda3f0ef274",
      "date": "2025-09-27",
      "description": "Mother's Day Shopping",
      "amount": 1800,
      "category": "Other_Income",
      "type": "income",
      "subcategory": "Miscellaneous",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.3
    },
    {
      "id": "c8dcd477-7a89-471f-80f5-114f6993514f",
      "date": "2025-09-27",
      "description": "Father's Day Gift",
      "amount": 2200,
      "category": "Other_Income",
      "type": "income",
      "subcategory": "Miscellaneous",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.3
    },
    {
      "id": "7a78542e-5025-4382-a14a-4a390754f449",
      "date": "2025-09-27",
      "description": "Monsoon Shopping - Clothes",
      "amount": 3500,
      "category": "Other_Income",
      "type": "income",
      "subcategory": "Miscellaneous",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.3
    },
    {
      "id": "a05ca252-16a2-4b19-9892-402c5725ed34",
      "date": "2025-09-27",
      "description": "Independence Day Shopping",
      "amount": 1500,
      "category": "Other_Income",
      "type": "income",
      "subcategory": "Miscellaneous",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.3
    },
    {
      "id": "fa7af61d-2cca-4c47-bea6-9d0e3a0dae11",
      "date": "2025-09-27",
      "description": "Festival Shopping - Ganesh Chaturthi",
      "amount": 4000,
      "category": "Other_Income",
      "type": "income",
      "subcategory": "Miscellaneous",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.3
    },
    {
      "id": "8ea06735-e29e-4a51-9722-7dfefc0ab6f6",
      "date": "2025-09-27",
      "description": "Diwali Shopping",
      "amount": 8000,
      "category": "Other_Income",
      "type": "income",
      "subcategory": "Miscellaneous",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.3
    },
    {
      "id": "b6860f1a-37f3-406b-957a-460dffa99d5e",
      "date": "2025-09-27",
      "description": "Children's Day Gift",
      "amount": 1200,
      "category": "Other_Income",
      "type": "income",
      "subcategory": "Miscellaneous",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.3
    },
    {
      "id": "bc5a8a16-265a-4470-bdd8-ab17104ad90b",
      "date": "2025-09-27",
      "description": "Christmas Shopping",
      "amount": 6000,
      "category": "Other_Income",
      "type": "income",
      "subcategory": "Miscellaneous",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.3
    },
    {
      "id": "3e2b177f-6b67-4622-a2b0-d14bc36e9cac",
      "date": "2025-09-27",
      "description": "FD Interest Credit - ICICI",
      "amount": 2500,
      "category": "Income",
      "type": "income",
      "subcategory": "Investment_Returns",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.9
    },
    {
      "id": "13dd51e6-431e-4804-904c-c837a6479c11",
      "date": "2025-09-27",
      "description": "FD Interest Credit - ICICI",
      "amount": 2500,
      "category": "Income",
      "type": "income",
      "subcategory": "Investment_Returns",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.9
    },
    {
      "id": "991652f5-a1ce-4d65-bf67-94eee50cd4d2",
      "date": "2025-09-27",
      "description": "FD Interest Credit - ICICI",
      "amount": 2500,
      "category": "Income",
      "type": "income",
      "subcategory": "Investment_Returns",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.9
    },
    {
      "id": "f1e64bb3-5222-4f99-bd3b-5bf23faae814",
      "date": "2025-09-27",
      "description": "FD Interest Credit - ICICI",
      "amount": 2500,
      "category": "Income",
      "type": "income",
      "subcategory": "Investment_Returns",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.9
    },
    {
      "id": "d4dc59b7-f0a0-4986-ac06-20a34c6f18e4",
      "date": "2025-09-27",
      "description": "Gym Membership - Gold's Gym",
      "amount": 2500,
      "category": "Other_Income",
      "type": "income",
      "subcategory": "Miscellaneous",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.3
    },
    {
      "id": "ec58d9ca-a96e-4979-9b4e-fa5fc0759b23",
      "date": "2025-09-27",
      "description": "Gym Membership Renewal - Gold's Gym",
      "amount": 2500,
      "category": "Other_Income",
      "type": "income",
      "subcategory": "Miscellaneous",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.3
    },
    {
      "id": "21818d4d-5341-43e0-aaca-d90db71f9b07",
      "date": "2025-09-27",
      "description": "Car Service - Maruti Service",
      "amount": 3500,
      "category": "Other_Income",
      "type": "income",
      "subcategory": "Miscellaneous",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.3
    },
    {
      "id": "b5970c3b-c637-436e-af96-4f07e5b3358d",
      "date": "2025-09-27",
      "description": "Car Service - Maruti Service",
      "amount": 4200,
      "category": "Other_Income",
      "type": "income",
      "subcategory": "Miscellaneous",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.3
    },
    {
      "id": "e2539643-39d7-4047-b647-7a72a9c7920b",
      "date": "2025-09-27",
      "description": "Home Maintenance - Plumbing",
      "amount": 2800,
      "category": "Other_Income",
      "type": "income",
      "subcategory": "Miscellaneous",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.3
    },
    {
      "id": "75422026-9f86-4e51-b75e-366e1d086b43",
      "date": "2025-09-27",
      "description": "Home Maintenance - Painting",
      "amount": 8500,
      "category": "Other_Income",
      "type": "income",
      "subcategory": "Miscellaneous",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.3
    },
    {
      "id": "f4256353-3aa0-429e-88a3-54c16f50e156",
      "date": "2025-09-27",
      "description": "Vacation - Flight Booking",
      "amount": 12000,
      "category": "Other_Income",
      "type": "income",
      "subcategory": "Miscellaneous",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.3
    },
    {
      "id": "fd8df97d-a190-460c-9c63-b0e194ca5b9e",
      "date": "2025-09-27",
      "description": "Vacation - Hotel Booking",
      "amount": 8000,
      "category": "Other_Income",
      "type": "income",
      "subcategory": "Miscellaneous",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.3
    },
    {
      "id": "739ca4cc-aa39-4eb2-bca3-56d82bfc454c",
      "date": "2025-09-27",
      "description": "Electronics - Laptop Purchase",
      "amount": 45000,
      "category": "Other_Income",
      "type": "income",
      "subcategory": "Miscellaneous",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.3
    },
    {
      "id": "65349112-472e-41da-9b87-0cca04a066ba",
      "date": "2025-09-27",
      "description": "Education - Online Course Udemy",
      "amount": 2999,
      "category": "Other_Income",
      "type": "income",
      "subcategory": "Miscellaneous",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.3
    },
    {
      "id": "14ac456c-51de-4ae2-bf7c-272bec4915e3",
      "date": "2025-09-27",
      "description": "Education - Certification Fee",
      "amount": 5000,
      "category": "Other_Income",
      "type": "income",
      "subcategory": "Miscellaneous",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.3
    },
    {
      "id": "38e0e653-bbed-4376-bdd5-8f27a4857708",
      "date": "2025-09-27",
      "description": "Bank Charges",
      "amount": 150,
      "category": "Other_Income",
      "type": "income",
      "subcategory": "Miscellaneous",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.3
    },
    {
      "id": "4c7f1605-014b-4626-961a-8c259ba37251",
      "date": "2025-09-27",
      "description": "Bank Charges",
      "amount": 150,
      "category": "Other_Income",
      "type": "income",
      "subcategory": "Miscellaneous",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.3
    },
    {
      "id": "aa7480a4-7e22-4d5a-b02f-02e723d30591",
      "date": "2025-09-27",
      "description": "Bank Charges",
      "amount": 150,
      "category": "Other_Income",
      "type": "income",
      "subcategory": "Miscellaneous",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.3
    },
    {
      "id": "8aa6b337-1c7e-4748-a66e-711e6c87762c",
      "date": "2025-09-27",
      "description": "Bank Charges",
      "amount": 150,
      "category": "Other_Income",
      "type": "income",
      "subcategory": "Miscellaneous",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.3
    },
    {
      "id": "460ca537-9288-4e53-b7a5-95233fd6a009",
      "date": "2025-09-27",
      "description": "Bank Charges",
      "amount": 150,
      "category": "Other_Income",
      "type": "income",
      "subcategory": "Miscellaneous",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.3
    },
    {
      "id": "370cc83d-379b-40b5-8ae6-91427392d888",
      "date": "2025-09-27",
      "description": "Bank Charges",
      "amount": 150,
      "category": "Other_Income",
      "type": "income",
      "subcategory": "Miscellaneous",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.3
    },
    {
      "id": "b3c516c0-f70f-4e64-83b7-789de16fd362",
      "date": "2025-09-27",
      "description": "Bank Charges",
      "amount": 150,
      "category": "Other_Income",
      "type": "income",
      "subcategory": "Miscellaneous",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.3
    },
    {
      "id": "df77ca62-1ade-448f-9291-26e5d2216cbc",
      "date": "2025-09-27",
      "description": "Bank Charges",
      "amount": 150,
      "category": "Other_Income",
      "type": "income",
      "subcategory": "Miscellaneous",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.3
    },
    {
      "id": "8ea62411-0afc-4292-b65a-045dc8dcbeb4",
      "date": "2025-09-27",
      "description": "Bank Charges",
      "amount": 150,
      "category": "Other_Income",
      "type": "income",
      "subcategory": "Miscellaneous",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.3
    },
    {
      "id": "09757d44-f874-49b3-8d8a-1f0a885059a3",
      "date": "2025-09-27",
      "description": "Bank Charges",
      "amount": 150,
      "category": "Other_Income",
      "type": "income",
      "subcategory": "Miscellaneous",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.3
    },
    {
      "id": "ede79646-954e-4b54-8b92-689b8472f043",
      "date": "2025-09-27",
      "description": "Bank Charges",
      "amount": 150,
      "category": "Other_Income",
      "type": "income",
      "subcategory": "Miscellaneous",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.3
    },
    {
      "id": "ba2fcba2-0f82-4686-8453-9cc1eee3b4ae",
      "date": "2025-09-27",
      "description": "Bank Charges",
      "amount": 150,
      "category": "Other_Income",
      "type": "income",
      "subcategory": "Miscellaneous",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.3
    },
    {
      "id": "c3ced5a0-634a-4c14-8f99-8dc1b30be464",
      "date": "2025-09-27",
      "description": "Freelance Income - Web Design",
      "amount": 15000,
      "category": "Income",
      "type": "income",
      "subcategory": "Salary",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.95
    },
    {
      "id": "3bbcb826-7b86-471f-af75-796517a3acf4",
      "date": "2025-09-27",
      "description": "Freelance Income - Consulting",
      "amount": 20000,
      "category": "Income",
      "type": "income",
      "subcategory": "Salary",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.95
    },
    {
      "id": "5ee7ee4a-4c8f-4af1-84ec-4f11a0bd223e",
      "date": "2025-09-27",
      "description": "Freelance Income - App Development",
      "amount": 25000,
      "category": "Income",
      "type": "income",
      "subcategory": "Salary",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.95
    }
  ],
  "investment_transactions": [
    {
      "id": "afc3665a-187a-4c8b-a675-15fc994d013a",
      "date": "2025-09-27",
      "description": "SIP ELSS Mutual Fund - Axis",
      "amount": 5000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    },
    {
      "id": "957fa3d9-ad4e-478f-94a1-0a0e997e3f1f",
      "date": "2025-09-27",
      "description": "SIP ELSS Mutual Fund - Axis",
      "amount": 5000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    },
    {
      "id": "562eb21a-d1b4-4453-bb7f-b53bfaf0472c",
      "date": "2025-09-27",
      "description": "SIP ELSS Mutual Fund - Axis",
      "amount": 5000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    },
    {
      "id": "a2e411bf-860a-4ead-9c1b-e310444e8121",
      "date": "2025-09-27",
      "description": "SIP ELSS Mutual Fund - Axis",
      "amount": 5000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    },
    {
      "id": "72cb3589-171e-491e-8115-aaf7f8f38b80",
      "date": "2025-09-27",
      "description": "SIP ELSS Mutual Fund - Axis",
      "amount": 5000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    },
    {
      "id": "17a02df0-c2a2-46ea-ae10-496c9a2fafc7",
      "date": "2025-09-27",
      "description": "SIP ELSS Mutual Fund - Axis",
      "amount": 5000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    },
    {
      "id": "7aa55fd9-7e00-4e53-b854-0e9158c9b587",
      "date": "2025-09-27",
      "description": "SIP ELSS Mutual Fund - Axis",
      "amount": 5000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    },
    {
      "id": "f4b6d15f-d4cf-4709-9c6d-c5b5de340ff4",
      "date": "2025-09-27",
      "description": "SIP ELSS Mutual Fund - Axis",
      "amount": 5000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    },
    {
      "id": "3265444e-2cd9-4e8b-91d2-9ad149efe201",
      "date": "2025-09-27",
      "description": "SIP ELSS Mutual Fund - Axis",
      "amount": 5000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    },
    {
      "id": "a53e0d8e-6be1-4c37-8984-cc3d946572fd",
      "date": "2025-09-27",
      "description": "SIP ELSS Mutual Fund - Axis",
      "amount": 5000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    },
    {
      "id": "40617a75-a20a-4ce6-8a65-2b1307570849",
      "date": "2025-09-27",
      "description": "SIP ELSS Mutual Fund - Axis",
      "amount": 5000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    },
    {
      "id": "4b7e8bbc-e75c-4b7c-a9e1-15132608ca1d",
      "date": "2025-09-27",
      "description": "SIP ELSS Mutual Fund - Axis",
      "amount": 5000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    },
    {
      "id": "1ee1602c-fb96-46fd-86df-7f07db25200f",
      "date": "2025-09-27",
      "description": "PPF Contribution - SBI",
      "amount": 2000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "PF_PPF",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.95
    },
    {
      "id": "70bbdca3-6cd7-464f-811d-945133313a64",
      "date": "2025-09-27",
      "description": "PPF Contribution - SBI",
      "amount": 2000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "PF_PPF",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.95
    },
    {
      "id": "16462e7f-d3fe-45e7-8438-e8ce7a8cb85f",
      "date": "2025-09-27",
      "description": "PPF Contribution - SBI",
      "amount": 2000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "PF_PPF",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.95
    },
    {
      "id": "6dbad8bd-42f3-4b18-8702-7d8648ab65c4",
      "date": "2025-09-27",
      "description": "PPF Contribution - SBI",
      "amount": 2000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "PF_PPF",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.95
    },
    {
      "id": "ca394374-83e1-4188-b22b-4773577e0844",
      "date": "2025-09-27",
      "description": "PPF Contribution - SBI",
      "amount": 2000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "PF_PPF",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.95
    },
    {
      "id": "a0a03d92-e2e0-4b8d-a86e-7fc58a803389",
      "date": "2025-09-27",
      "description": "PPF Contribution - SBI",
      "amount": 2000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "PF_PPF",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.95
    },
    {
      "id": "51d29191-1702-446c-8283-55ac3694b72d",
      "date": "2025-09-27",
      "description": "PPF Contribution - SBI",
      "amount": 2000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "PF_PPF",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.95
    },
    {
      "id": "7ef199c6-2657-46ed-9d58-88afce046753",
      "date": "2025-09-27",
      "description": "PPF Contribution - SBI",
      "amount": 2000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "PF_PPF",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.95
    },
    {
      "id": "874d781b-6b7e-4a5e-b44a-95d45785ed96",
      "date": "2025-09-27",
      "description": "PPF Contribution - SBI",
      "amount": 2000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "PF_PPF",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.95
    },
    {
      "id": "8a2cc156-dac9-4af5-a774-57f86ddf082d",
      "date": "2025-09-27",
      "description": "PPF Contribution - SBI",
      "amount": 2000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "PF_PPF",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.95
    },
    {
      "id": "bccc1063-1aec-467a-bb80-a572b83dcde2",
      "date": "2025-09-27",
      "description": "PPF Contribution - SBI",
      "amount": 2000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "PF_PPF",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.95
    },
    {
      "id": "4c7a218f-8656-4737-ba1a-5dc3a8aeff0c",
      "date": "2025-09-27",
      "description": "PPF Contribution - SBI",
      "amount": 2000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "PF_PPF",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.95
    },
    {
      "id": "718025ec-4d98-44c1-a178-d085e0f22b02",
      "date": "2025-09-27",
      "description": "Investment - Mutual Fund SIP",
      "amount": 3000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    },
    {
      "id": "02e1b9d3-fd19-4454-ba4a-2de85603a06e",
      "date": "2025-09-27",
      "description": "Investment - Mutual Fund SIP",
      "amount": 3000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    },
    {
      "id": "b4b9c0f5-9b6b-49d7-983a-18d895ce49e3",
      "date": "2025-09-27",
      "description": "Investment - Mutual Fund SIP",
      "amount": 3000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    },
    {
      "id": "97fbd792-7e86-46f1-aa34-47dd12c4a8aa",
      "date": "2025-09-27",
      "description": "Investment - Mutual Fund SIP",
      "amount": 3000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    },
    {
      "id": "7ae3aba8-4899-4f95-a7d0-e6e564ef5e75",
      "date": "2025-09-27",
      "description": "Investment - Mutual Fund SIP",
      "amount": 3000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    },
    {
      "id": "8c49aa52-f5c2-4293-b855-697a2554d3b7",
      "date": "2025-09-27",
      "description": "Investment - Mutual Fund SIP",
      "amount": 3000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    },
    {
      "id": "297695ae-d261-4a20-9c18-4d1cb9d0ee30",
      "date": "2025-09-27",
      "description": "Investment - Mutual Fund SIP",
      "amount": 3000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    },
    {
      "id": "3ade0893-54a4-4c23-9ca1-795eac70944f",
      "date": "2025-09-27",
      "description": "Investment - Mutual Fund SIP",
      "amount": 3000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    },
    {
      "id": "e5a95580-ed03-4a88-95a7-8f03e3edfbd0",
      "date": "2025-09-27",
      "description": "Investment - Mutual Fund SIP",
      "amount": 3000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    },
    {
      "id": "22ba6a56-0178-4806-86af-f504c4176806",
      "date": "2025-09-27",
      "description": "Investment - Mutual Fund SIP",
      "amount": 3000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    },
    {
      "id": "60f7ad95-a268-4508-8250-bac56e2327f6",
      "date": "2025-09-27",
      "description": "Investment - Mutual Fund SIP",
      "amount": 3000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    },
    {
      "id": "0ce593ab-693b-423e-a42b-95d37e8956f8",
      "date": "2025-09-27",
      "description": "Investment - Mutual Fund SIP",
      "amount": 3000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    }
  ],
  "deduction_eligible_expenses": [
    {
      "id": "afc3665a-187a-4c8b-a675-15fc994d013a",
      "date": "2025-09-27",
      "description": "SIP ELSS Mutual Fund - Axis",
      "amount": 5000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    },
    {
      "id": "957fa3d9-ad4e-478f-94a1-0a0e997e3f1f",
      "date": "2025-09-27",
      "description": "SIP ELSS Mutual Fund - Axis",
      "amount": 5000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    },
    {
      "id": "562eb21a-d1b4-4453-bb7f-b53bfaf0472c",
      "date": "2025-09-27",
      "description": "SIP ELSS Mutual Fund - Axis",
      "amount": 5000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    },
    {
      "id": "a2e411bf-860a-4ead-9c1b-e310444e8121",
      "date": "2025-09-27",
      "description": "SIP ELSS Mutual Fund - Axis",
      "amount": 5000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    },
    {
      "id": "72cb3589-171e-491e-8115-aaf7f8f38b80",
      "date": "2025-09-27",
      "description": "SIP ELSS Mutual Fund - Axis",
      "amount": 5000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    },
    {
      "id": "17a02df0-c2a2-46ea-ae10-496c9a2fafc7",
      "date": "2025-09-27",
      "description": "SIP ELSS Mutual Fund - Axis",
      "amount": 5000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    },
    {
      "id": "7aa55fd9-7e00-4e53-b854-0e9158c9b587",
      "date": "2025-09-27",
      "description": "SIP ELSS Mutual Fund - Axis",
      "amount": 5000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    },
    {
      "id": "f4b6d15f-d4cf-4709-9c6d-c5b5de340ff4",
      "date": "2025-09-27",
      "description": "SIP ELSS Mutual Fund - Axis",
      "amount": 5000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    },
    {
      "id": "3265444e-2cd9-4e8b-91d2-9ad149efe201",
      "date": "2025-09-27",
      "description": "SIP ELSS Mutual Fund - Axis",
      "amount": 5000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    },
    {
      "id": "a53e0d8e-6be1-4c37-8984-cc3d946572fd",
      "date": "2025-09-27",
      "description": "SIP ELSS Mutual Fund - Axis",
      "amount": 5000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    },
    {
      "id": "40617a75-a20a-4ce6-8a65-2b1307570849",
      "date": "2025-09-27",
      "description": "SIP ELSS Mutual Fund - Axis",
      "amount": 5000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    },
    {
      "id": "4b7e8bbc-e75c-4b7c-a9e1-15132608ca1d",
      "date": "2025-09-27",
      "description": "SIP ELSS Mutual Fund - Axis",
      "amount": 5000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    },
    {
      "id": "1ee1602c-fb96-46fd-86df-7f07db25200f",
      "date": "2025-09-27",
      "description": "PPF Contribution - SBI",
      "amount": 2000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "PF_PPF",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.95
    },
    {
      "id": "70bbdca3-6cd7-464f-811d-945133313a64",
      "date": "2025-09-27",
      "description": "PPF Contribution - SBI",
      "amount": 2000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "PF_PPF",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.95
    },
    {
      "id": "16462e7f-d3fe-45e7-8438-e8ce7a8cb85f",
      "date": "2025-09-27",
      "description": "PPF Contribution - SBI",
      "amount": 2000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "PF_PPF",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.95
    },
    {
      "id": "6dbad8bd-42f3-4b18-8702-7d8648ab65c4",
      "date": "2025-09-27",
      "description": "PPF Contribution - SBI",
      "amount": 2000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "PF_PPF",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.95
    },
    {
      "id": "ca394374-83e1-4188-b22b-4773577e0844",
      "date": "2025-09-27",
      "description": "PPF Contribution - SBI",
      "amount": 2000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "PF_PPF",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.95
    },
    {
      "id": "a0a03d92-e2e0-4b8d-a86e-7fc58a803389",
      "date": "2025-09-27",
      "description": "PPF Contribution - SBI",
      "amount": 2000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "PF_PPF",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.95
    },
    {
      "id": "51d29191-1702-446c-8283-55ac3694b72d",
      "date": "2025-09-27",
      "description": "PPF Contribution - SBI",
      "amount": 2000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "PF_PPF",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.95
    },
    {
      "id": "7ef199c6-2657-46ed-9d58-88afce046753",
      "date": "2025-09-27",
      "description": "PPF Contribution - SBI",
      "amount": 2000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "PF_PPF",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.95
    },
    {
      "id": "874d781b-6b7e-4a5e-b44a-95d45785ed96",
      "date": "2025-09-27",
      "description": "PPF Contribution - SBI",
      "amount": 2000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "PF_PPF",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.95
    },
    {
      "id": "8a2cc156-dac9-4af5-a774-57f86ddf082d",
      "date": "2025-09-27",
      "description": "PPF Contribution - SBI",
      "amount": 2000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "PF_PPF",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.95
    },
    {
      "id": "bccc1063-1aec-467a-bb80-a572b83dcde2",
      "date": "2025-09-27",
      "description": "PPF Contribution - SBI",
      "amount": 2000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "PF_PPF",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.95
    },
    {
      "id": "4c7a218f-8656-4737-ba1a-5dc3a8aeff0c",
      "date": "2025-09-27",
      "description": "PPF Contribution - SBI",
      "amount": 2000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "PF_PPF",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.95
    },
    {
      "id": "718025ec-4d98-44c1-a178-d085e0f22b02",
      "date": "2025-09-27",
      "description": "Investment - Mutual Fund SIP",
      "amount": 3000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    },
    {
      "id": "02e1b9d3-fd19-4454-ba4a-2de85603a06e",
      "date": "2025-09-27",
      "description": "Investment - Mutual Fund SIP",
      "amount": 3000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    },
    {
      "id": "b4b9c0f5-9b6b-49d7-983a-18d895ce49e3",
      "date": "2025-09-27",
      "description": "Investment - Mutual Fund SIP",
      "amount": 3000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    },
    {
      "id": "97fbd792-7e86-46f1-aa34-47dd12c4a8aa",
      "date": "2025-09-27",
      "description": "Investment - Mutual Fund SIP",
      "amount": 3000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    },
    {
      "id": "7ae3aba8-4899-4f95-a7d0-e6e564ef5e75",
      "date": "2025-09-27",
      "description": "Investment - Mutual Fund SIP",
      "amount": 3000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    },
    {
      "id": "8c49aa52-f5c2-4293-b855-697a2554d3b7",
      "date": "2025-09-27",
      "description": "Investment - Mutual Fund SIP",
      "amount": 3000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    },
    {
      "id": "297695ae-d261-4a20-9c18-4d1cb9d0ee30",
      "date": "2025-09-27",
      "description": "Investment - Mutual Fund SIP",
      "amount": 3000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    },
    {
      "id": "3ade0893-54a4-4c23-9ca1-795eac70944f",
      "date": "2025-09-27",
      "description": "Investment - Mutual Fund SIP",
      "amount": 3000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    },
    {
      "id": "e5a95580-ed03-4a88-95a7-8f03e3edfbd0",
      "date": "2025-09-27",
      "description": "Investment - Mutual Fund SIP",
      "amount": 3000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    },
    {
      "id": "22ba6a56-0178-4806-86af-f504c4176806",
      "date": "2025-09-27",
      "description": "Investment - Mutual Fund SIP",
      "amount": 3000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    },
    {
      "id": "60f7ad95-a268-4508-8250-bac56e2327f6",
      "date": "2025-09-27",
      "description": "Investment - Mutual Fund SIP",
      "amount": 3000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    },
    {
      "id": "0ce593ab-693b-423e-a42b-95d37e8956f8",
      "date": "2025-09-27",
      "description": "Investment - Mutual Fund SIP",
      "amount": 3000,
      "category": "Investment",
      "type": "investment",
      "subcategory": "Tax_Saving",
      "is_recurring": false,
      "source_file": "Demo.csv",
      "confidence_score": 0.85
    }
  ],
  "tax_optimization": {
    "remaining_80c_limit": 30000,
    "potential_tax_saving": 9000,
    "current_deductions": 120000,
    "recommendations": {
      "increase_80c_investments": false,
      "consider_nps": true,
      "health_insurance_adequate": false
    }
  },
  "projected_tax_liability": {
    "gross_income": 9360000,
    "total_deductions": 120000,
    "taxable_income": 9190000,
    "estimated_tax": 1838000
  }
}
```

### Output: 
```
{
  "deduction_optimization": {
    "optimization_suggestions": [
      {
        "potential_tax_saving": 10296,
        "reasoning": "Based on your transactions described as 'Freelance Income - Web Design' (\u20b915,000), 'Freelance Income - Consulting' (\u20b920,000), and 'Freelance Income - App Development' (\u20b925,000), you have a total professional income of \u20b960,000. Under Section 44ADA of the Income Tax Act, you can declare 50% of this (\u20b930,000) as your profit. The remaining \u20b930,000 is treated as a deductible expense. This is a simplified method that often proves more beneficial than tracking individual small expenses.",
        "section": "Section 44ADA",
        "sources": [
          {
            "title": "Section 44ADA Presumptive Tax for Professionals - Tata AIA",
            "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwuaeUaGQmKZau5YTSFJTidHt4v1jwXkBaufe9iqHeNaejGHGGhnUeE6Z4u_4F3SVA_1fh3gPucd_tsYw7CasGsI4DIJFwgB5pLawLXs2x3nZqyoyPwpfzOfxDYZwiOxXlUqt3q4KGwcyVPl7sb82c54f-Lq5-a94hybm1zyMy8Cw2Wto="
          },
          {
            "title": "Section 44ADA: What is the Presumptive Tax Scheme for Professionals? - TaxBuddy.com",
            "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGVdbl69S-x1bHEaHLtOYHPQkobiiovvZb-iK7XVjrbsG3qHvHNgIz_jnNg4fUj8S9FplUFnng2k6HKdXVfv6YnwA2LJKFm6woMcD_ZdCzT-ct7iCFrvuNgvUh-xxpi-wAlobnkjQWKZ71WLcMfCp_Xdu8AhTds9lplbR3dwaA4Dh-QyGhIP7FkIWwGCwbcGYBjgrU3xesCmrVF5Q=="
          },
          {
            "title": "Section 44ADA \u2013 Presumptive Tax Scheme for Professionals - ClearTax",
            "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEC7I_YV8FT-PpSymvdM5TghKpbkYcZ9r7JNN_Mtk8Tb4IW56fqLNgWAl7WUSbL1kiUAvgwGe2ZOstfqh2uR2EVRazzWxGBkQHLNPHw1hlB0yprg2woicY0N3ARQzc-"
          },
          {
            "title": "Guide to 44ADA of Income Tax Act: Presumptive Tax Scheme - Skydo",
            "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEg7neflDICKrTA2Ffxv7Bp-ldoPD16eWuVDQ0w3woc69rEjYmWCtVHlAtyHnlRFrMIYd510LAahD4w3PLU9H2xB1N5BJFy6t7a5NlwHgCw7_iUwjz_bX2s1OCm3Dr25j2s9DKwiLMzdZeJNvXm"
          }
        ],
        "suggestion": "Adopt the Presumptive Taxation Scheme for your freelance income to simplify tax filing and potentially lower your tax liability. Under this scheme, 50% of your gross freelance receipts are considered as your taxable income, without the need to maintain detailed expense records."
      },
      {
        "potential_tax_saving": 25740,
        "reasoning": "Your transaction history does not show any payments for health insurance premiums. The Income Tax Act provides a deduction under Section 80D for such premiums. You can claim up to \u20b925,000 for policies covering yourself, your spouse, and dependent children. An additional deduction is available for premiums paid for your parents' insurance, up to \u20b925,000 (if they are below 60) or up to \u20b950,000 (if they are senior citizens). Assuming you get coverage for yourself (\u20b925,000 limit) and senior citizen parents (\u20b950,000 limit), you could claim a total deduction of \u20b975,000.",
        "section": "Section 80D",
        "sources": [
          {
            "title": "Section 80D Income Tax | Deductions for Health & Medical Insurance",
            "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEun0xMeAO9ecYC45gRWBK27ilFgaClpFqPKvrAx9EMXatx7B1aifFi-ZOpcmUCONKzjHbuGwd8209r0l6BHvfApXYA1GBqmtgIsM3OM2X0njlzdcPRbIYNTnYF9PJpqTrk3M9QAhU="
          },
          {
            "title": "Section 80D: Deductions for Medical & Health Insurance - Policybazaar",
            "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkAaZiwB-5FUGeYvqiIcRvn-0E5DYVO8mLA6d2C51pdeG9nD8f075KLSgYRACNjuWgFjBd1FBFS9ucp3YgIePLL4ULV50I1efC80zmzF0MYnh6tZfy5ayUT6m4F6HocuV3pKr1mYwwEmSX8MwceqOMe1ghaq8y3hA5f4A30Suj"
          },
          {
            "title": "Section 80D - All about Deductions for Medical and Health Insurance - HDFC Life",
            "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_7nVfwUVgPjzwIcUZTDbL7Bm28tMXHaYF1i6srYR0s9si67vrhM_NDPcmI0Pg6LAWb0nDesBBK8aDBVQ3xRiUYJTqfmG4uV7m2dqrzcWPPwEUlHW7MbD0jUMEigfEHpQvImSd1wDXFhZBdq3pa8Tojt3rWg0jEDJACiYyo_ga4plcZEvrq-ARSX79BT7ceFRlgAKH4K8OObg="
          },
          {
            "title": "Section 80D of Income Tax Act: Deductions Under Medical Insurance, Limit, Eligibility And Policies - ClearTax",
            "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG2htinoXhP5QzytHiCbQDyrOsGD_jdsWgYNPrKvUUrEg7eXnnX0ZbYHofJLZsfjvhYdU4lqkqnKGH76w3KKjvagnPg_uff0WnLN0yQCnWmDYsPD8DlTM7sIXHetTHk7HGLjg=="
          },
          {
            "title": "Section 80D - Tax Benefits & Deductions on Health Insurance",
            "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYH0rjYCHyBdwkH5f-Z_Y1l_jAz9yfKQW6uWvoBFVfutL4gKZnbTGE8ra91ZuH-mf4PscWBVDgtou85eB3tctmRbgQO2xZfLo4EEd5QmfiZa0DtyGvsIzYVU9h6pJ5_saGouLvapilINkAXIcyeGsgudG7VtVlaFRlp07YAPRRXsc7OvgNRxb_mZ5BgFtf46Phy6PKwcQeJw=="
          }
        ],
        "suggestion": "Purchase a health insurance policy for yourself, your family, and your parents to claim a significant tax deduction. You can claim up to \u20b925,000 for self/family and an additional amount of up to \u20b950,000 for senior citizen parents."
      },
      {
        "potential_tax_saving": 17160,
        "reasoning": "Your transaction data does not indicate any investments in the National Pension System (NPS). Section 80CCD(1B) of the Income Tax Act allows for an exclusive tax deduction of up to \u20b950,000 for contributions to an NPS Tier I account. This benefit is in addition to the deductions you can claim under Section 80C, allowing you to save tax on a total of \u20b92 lakh (\u20b91.5 lakh under 80C + \u20b950,000 under 80CCD(1B)).",
        "section": "Section 80CCD(1B)",
        "sources": [
          {
            "title": "Deductions Under Section 80CCD(1B) of Income Tax - ClearTax",
            "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYOqdzL3gSK_6XbBGHbIUydLgjUCQpWWJENlktpHGwigH-NX_Vssz-GULvTRx-PqK06R7N4LTNofx9rNotl_lvPA4rK2IOnCXUPTFDmdX_W-n4hPf2vckuTr5LgI5SUr-d7w=="
          },
          {
            "title": "NPS Deduction Under Section 80CCD: Comprehensive Guide - Protean",
            "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6ORQARvoupenswZDLBFKq0CdqLdN94I5AQUYQk1HlcOjE8EOVvV8q0DFCeoxSsf-bjZ1WsXkzC2PaF5kl2eyrb93fhU5nGcrO3I-2qJNvZdaqGYtmvjnxyyJqSMzuedG_112pDSFgA2-t_PAb5zfNrYsmZqjxltNQuw8Nxvv1nA=="
          },
          {
            "title": "Tax Benefits under NPS - NPScra.nsdl.co.in",
            "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQES5H317d7sWJINsRBBTw-dvOkfMrdJCH-vO2-ptsxAiRvkLGZak2JU-YENswBd4l-FwYOUnz1YM5O2D_v8ev7jQkHKicJBhZPCy7c46hLkSp3KsuKivFciGbngSu3AaMP-VKYXPOF1mAfpSXpLE-PBCQhbp07Ox_dh26Z1_hCWXzydSjY="
          },
          {
            "title": "Understanding NPS tax benefits in the Old and New Regime - Protean",
            "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFp1yUM3J_UCx6-neYxzg_DUBPL76_xsT7LgynUVenj-GC95xN9RxJg23OU5F-NpKOvBrugXilG0RjkHGKZSncTpI5VqlRWhk1Itt4e-4k__WKcHAtznWch0tERn3-3cGXN1Qu366C_66l_7AUU_CK234SReqqJ9Snx_69owQ=="
          }
        ],
        "suggestion": "Invest up to \u20b950,000 in the National Pension System (NPS) to claim an additional tax deduction. This deduction is over and above the \u20b91.5 lakh limit of Section 80C."
      },
      {
        "potential_tax_saving": 10296,
        "reasoning": "Based on your transactions 'SIP ELSS Mutual Fund - Axis' (\u20b960,000 total) and 'PPF Contribution - SBI' (\u20b924,000 total), and assuming your 'Investment - Mutual Fund SIP' (\u20b936,000 total) is also an ELSS, you have invested \u20b91,20,000. Section 80C of the Income Tax Act allows a maximum deduction of \u20b91,50,000. You have a remaining gap of \u20b930,000. You can invest this amount in options like PPF, ELSS, or Tax-Saving Fixed Deposits to utilize the full deduction limit.",
        "section": "Section 80C",
        "sources": [
          {
            "title": "Section 80C of Income Tax Act - Deductions U/S 80C - Bajaj Finserv",
            "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7nXFzaQMz0d8wRdGUNuRUpVLzf4SpLtIr9mt3TH943ojnxITq4YLP-qFBIJCbpYNw6q2bmbrdy64xovascTmQ5SVAbjqHBR2yVKjJ7ZAzcHi6A92Ebg4UtYy5IVaN4Dj1IyMG6GT_wYSj1AleYA=="
          },
          {
            "title": "Section 80C of Income Tax Act - 80C Deduction List - ClearTax",
            "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8AanAI-IDVXD9M_mbYhMirPUBiqyLMkw6AY2w5i8ms1VYB3AdvHFYgng_wJL3XTlmj9be0tEhsqras8AO1rvxwNJbP4JOiHU4RQQE89tKxk7s-p14OktvTCU14lNU53N7Sw=="
          },
          {
            "title": "How to Save Tax in India? 10 Smart and Legal Ways for FY 2025-26",
            "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHl9kwak1PRtJRPN0WZP3lg-ekXJUCn75GPqovrPR8tO18-Qd2miwqIsxZHu0ZKb6aauTL4_agjiYZFCE30un8wbksPRvXxaBGzNLEKqeYkQuORj3sOwjrMuk27r-A2ZPuQzqiODwbI8O9JeGUgW8SKTxwMg2dBeUjYLCvDVg7jLTE91anGL9AcbOT7XKsGqXXft-_iTLtOQ503Hji7tbbP7_g="
          }
        ],
        "suggestion": "Maximize your tax savings by investing an additional \u20b930,000 in eligible instruments to reach the full \u20b91.5 lakh limit under Section 80C."
      },
      {
        "potential_tax_saving": 8919,
        "reasoning": "This is an alternative if your actual expenses exceed 50% of your freelance income. Based on your transactions, you could claim depreciation on 'Electronics - Laptop Purchase' (\u20b945,000). The depreciation rate for laptops under Section 32 is 40%, allowing a deduction of \u20b918,000. Additionally, the 'Education - Online Course Udemy' (\u20b92,999) and 'Education - Certification Fee' (\u20b95,000) can be claimed as business expenses under Section 37(1). This totals \u20b925,999 in deductions. However, since this is less than the \u20b930,000 deemed expense under Section 44ADA, the presumptive scheme is currently more beneficial for you.",
        "section": "Section 32 & 37(1)",
        "sources": [
          {
            "title": "Computer, Laptop and Printer Depreciation Rate: How To Calculate, Formula, Examples - ClearTax",
            "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQM1hQRSy8sNu58CjTKNfw1F5-aECnOtmcCR9BRhhlejrsVbD8mt6ng-HrjRx_9YrTh-GqFiOcH24YopD2nglSXDLMSjYqBwd5vwk5h6HOSko2fTIlfCB2ywZ8QD1AiK_7jsARmRbiMLffPkhmf-SBTl24jP0BJ4JsMQ=="
          },
          {
            "title": "Computer Depreciation Rate Under Income Tax - TaxBuddy.com",
            "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzxUaVhTDK8R3agR3OVaDM6AxB_kzQCt-Uop67FIQbrZt-ZqnnPhWkjW9K1SJqz1UfXG8dC0uOY-_kc3DDabsMDC-f-WhU-ouq4gJIsUZBAdurqD9Q0HG_V9KhKA98rDbfekLs67e_NhwI5U-vP5IMzeIRtwJcIXGsohoynEk="
          },
          {
            "title": "Income Tax for Freelancers - ClearTax",
            "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXU9G4VB-eTd4CYMi8BzmJoFk09KwAAiX2AjLOZvrQ6VvjOgyNWobvqk7H5Qp1fxTDeCFWVA_qbWZcXU2VVJM2bhQ2insfq2QViPMP3-oi8bu35o8kJMRQQDMMNwqoLW1-NCidsuNO8NVARA=="
          },
          {
            "title": "Income Tax Filing For the Freelancers in India - BankBazaar",
            "url": "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEDEt8xjtp1lnkLlRtUuyE58MCnO5Dx5vjO3Hkg3JjR8XAuY4QKWgQBpKUrUIrwE-zxWl64MddW6SicMV9Q2Crv4VvGB-X7mi9bDOuVPUfWDJeFM6Ahxc7nysHfeZSww-KP29EGv8rXsoQnaMfdIg=="
          }
        ],
        "suggestion": "As an alternative to presumptive taxation (Section 44ADA), you can claim actual expenses incurred for your freelance work. This includes depreciation on assets like your laptop and costs for professional development courses."
      }
    ],
    "total_potential_savings": 72411
  },
  "income_analysis": {
    "annual_income": 9534699,
    "current_deductions": 120000,
    "monthly_income": 780000
  },
  "session_id": "6237d0b9-7bbb-4210-b622-862a9709d2b8",
  "tax_calculation": {
    "new_regime": {
      "effective_tax_rate": 27.68,
      "taxable_income": 9459699,
      "total_tax": 2639426
    },
    "old_regime": {
      "effective_tax_rate": 28.6,
      "taxable_income": 9364699,
      "total_tax": 2726786
    },
    "recommended_regime": "New Regime",
    "savings": 87360
  }
}
```
