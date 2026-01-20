# 🛡️ VouchVault: AI Audit Agent

**AI-powered financial auditing and compliance verification system.**

VouchVault is an intelligent agent designed to audit invoices, verify bank statements, and ensure tax compliance using advanced LLM reasoning.

## 🚀 Features

- **Automated Tax Compliance**: Verifies GST calculations on invoices (18% standard rate).
- **Vendor Verification**: uses fuzzy matching to reconcile invoice vendors with bank statement records.
- **Intelligent Analysis**: Uses Google Gemini to reason about discrepancies (e.g., slight amount mismatches due to fees).
- **Tool-Based Reasoning**: The agent uses specialized Python tools for precise calculations and data matching.

## 🛠️ Project Structure

```
├── main.py                # Entry point
├── requirements.txt       # Dependencies
├── vouchvault/
│   ├── analyst.py         # AI Analyst Agent (Gemini)
│   ├── tools.py           # Compliance & Matching Tools
│   ├── manager.py         # Orchestration Logic
│   └── config.py          # Configuration & Dummy Data
└── tests/                 # Unit tests
```

## ⚡ Quick Start

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure API Key**
   Create a `.env` file or export your key:
   ```bash
   export GOOGLE_API_KEY="your_api_key_here"
   ```

3. **Run the Agent**
   ```bash
   python main.py
   ```

## 🧪 Testing

Run the test suite to verify agent performance:
```bash
pytest
```
