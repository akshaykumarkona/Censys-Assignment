# Censys Host Dataset Summarizer

This project provides a **Streamlit UI** and a **FastAPI backend** powered by a **LangGraph + Gemini model agent** to analyze and summarize **Censys-style JSON host datasets**.  

It generates concise, human-readable summaries for each host, including details about:

- IP address and location  
- ASN and organization  
- DNS/OS info  
- Key services and vulnerabilities (CVE IDs, severity, CVSS scores)  
- Threat intelligence signals (risk levels, malware families, security labels)  

All results are formatted in **Markdown** for readability.

---


## Project Structure

```
├── ui.py # Streamlit frontend for uploading JSON and viewing summaries
├── backend.py # FastAPI backend that accepts JSON and calls the summarizer agent
├── summarizer.py # LangGraph workflow with Gemini LLM summarization logic
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```


---

## Installation

1. **Clone the repo**
```bash
git clone github link
cd censys_summarizer
```
2. **Create and activate a virtual environment**
```bash
python -m venv venv
venv\Scripts\activate      # Windows
```

3. **Install dependencies**

```bash 
pip install -r requirements.txt
```


## Running the App
1. **Start the FastAPI Backend**
```bash
uvicorn backend:app --reload
```

*API will be available at: http://localhost:8000*

*Swagger docs: http://localhost:8000/docs*

2. *Launch the UI*
```bash
streamlit run ui.py
```

## Usage

- Open the Streamlit UI.

- Upload a JSON file containing host scan data (Censys-style).

- Click Generate Summary for Dataset.

- View compact Markdown summaries for each host, including vulnerabilities and threat intel.

### Example Input
```bash
{
  "metadata": {
    "description": "Censys host data",
    "created_at": "2025-01-12",
    "hosts_count": 1,
    "ips_analyzed": ["203.0.113.42"]
  },
  "hosts": [
    {
      "ip": "203.0.113.42",
      "location": {
        "city": "Berlin",
        "country": "Germany",
        "country_code": "DE"
      },
      "services": [
        {
          "port": 22,
          "protocol": "SSH",
          "vulnerabilities": [
            {"cve_id": "CVE-2023-99999", "severity": "critical", "cvss_score": 9.9}
          ]
        }
      ],
      "threat_intelligence": {
        "security_labels": ["REMOTE_ACCESS"],
        "risk_level": "high"
      }
    }
  ]
}

```


### Example Output
```bash

The summarizer generates compact, Markdown-formatted host summaries:

- **IP**: 203.0.113.42  
- **Location**: Berlin, Germany (DE)  
- **Services**: SSH (port 22, OpenSSH, CVE-2023-99999, critical, CVSS 9.9)  
- **Threat Intel**: Risk = high, Label = REMOTE_ACCESS  

This host runs SSH with a critical vulnerability, making it a high-risk remote access target.
```

## Requirements

*Dependencies are listed in requirements.txt*:

- langgraph

- langchain-google-genai

- pydantic

- streamlit

- fastapi

- uvicorn

*Install all via: ```pip install -r requirements.txt```*

### Agent Workflow

The summarizer uses a LangGraph StateGraph workflow:

### *START → Summarize Node → END*


- Input JSON is passed to the summarize_host node.

- Gemini LLM generates a concise Markdown summary for each host.

- FastAPI returns the summary to the Streamlit UI for display.

## Future Improvements

- Add richer schema validation for input JSON via Pydantic.

- Extend UI to support batch uploads.

- Add export options for summaries (PDF/CSV).

- Deploy with Docker or Kubernetes for production use.