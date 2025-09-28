-----

# 💰 Financial Data Analysis Hub: Unified API

## ✨ Project Status

| Status | Version | Base URL |
| :--- | :--- | :--- |
| **🚀 DEPLOYED** | `v1.0.0 (Local-Stable)` | `https://web-production-556a5.up.railway.app` (Based on user confirmation) |

-----

## 🎯 Overview

The **Financial Data Analysis Hub** is a high-performance, unified FastAPI service designed to ingest raw financial statements (CSV/PDF) and immediately deliver comprehensive, actionable financial intelligence.

Built for efficiency, this API bypasses slow external dependencies where possible, using specialized local algorithms for robust analysis.

### Core Capabilities

  * **⚡ High-Speed Processing:** Asynchronously handles file uploads, falling back to a **realistic mock generator** for unparsable PDF data.
  * **🏦 Credit Score Simulation (CIBIL):** Calculates a derived CIBIL score based on payment consistency and debt-to-income ratios.
  * **⚖️ Dynamic Tax Analysis:** Performs mandatory Old Regime vs. New Regime tax calculations and provides **rule-based, customized optimization suggestions** to maximize savings.

-----

## 🛠️ Tech Stack

| Component | Purpose | Notes |
| :--- | :--- | :--- |
| **Backend** | `FastAPI`, `Uvicorn` | Modern, high-performance Python web framework. |
| **Data Processing** | `Pandas`, `Faker`, `pdfplumber` | Data ingestion, cleanup, mock generation, and text extraction. |
| **Hosting** | `Railway` | Containerized deployment environment. |
| **Core Intelligence**| **Custom Local Algorithms** | Handles all CIBIL scoring and Tax optimization logic internally for speed. |

-----

## 💡 Key Endpoints & How to Use

The API uses a two-step process: `POST` to upload and start a session, followed by `GET` requests using the returned `session_id`.

### 1\. Start Processing & Get Session ID

Upload your bank statement file(s) to initiate data extraction, classification, and initial analysis.

  * **Endpoint:** `POST /process-files`
  * **Body:** `multipart/form-data` (Field name: `files`)

| Status | Output |
| :--- | :--- |
| `200 OK` | Full `ProcessedFinancialData` JSON object, including the **`session_id`** (e.g., `ca60d1cd-ed1e-42db-91af-cf7c0f6e178a`). |

### 2\. Retrieve Detailed Analysis

Use the `session_id` to retrieve the final reports.

| Endpoint | Description |
| :--- | :--- |
| `GET /analyze-cibil/{session_id}` | Returns the calculated CIBIL score, score component breakdown, and actionable credit advice. |
| `GET /analyze-tax/{session_id}` | Returns the full tax calculation, comparison between Old/New regimes, and **custom deduction optimization suggestions.** |
| `GET /session-data/{session_id}` | Returns the complete, raw, processed data object (transactions, summaries, etc.). |

-----

## 💻 Example Usage (JavaScript `fetch`)

Here is how a frontend application would execute the full analysis pipeline using your base URL:

```javascript
const API_BASE_URL = 'https://web-production-556a5.up.railway.app';
const fileInput = document.getElementById('fileInput');
const file = fileInput.files[0];

async function fetchAnalysis(file) {
    // 1. UPLOAD FILE AND GET SESSION ID
    const formData = new FormData();
    formData.append('files', file);
    
    const uploadRes = await fetch(`${API_BASE_URL}/process-files`, { method: 'POST', body: formData });
    const { session_id } = await uploadRes.json();

    // 2. FETCH CIBIL AND TAX REPORTS CONCURRENTLY
    const [cibilRes, taxRes] = await Promise.all([
        fetch(`${API_BASE_URL}/analyze-cibil/${session_id}`),
        fetch(`${API_BASE_URL}/analyze-tax/${session_id}`)
    ]);

    const cibilData = await cibilRes.json();
    const taxData = await taxRes.json();
    
    console.log("CIBIL Score:", cibilData.cibil_score);
    console.log("Tax Savings:", taxData.tax_calculation.savings);

    return { cibilData, taxData };
}

// execute fetchAnalysis(file) on button click...
```

-----

## ⚠️ Stability & Performance Note

To ensure the fastest and most stable deployment on free hosting tiers, this API uses **local, rule-based algorithms** for complex advice. The high-latency, external AI API calls were removed to maintain deployment integrity and performance.