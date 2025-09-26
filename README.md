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
├── ui.py # Streamlit Frontend for uploading JSON and viewing summaries
├── backend.py # FastAPI Backend that accepts JSON and calls the Summarizer Agent
├── summarizer.py # LangGraph Agent workflow with Gemini LLM and Prompt used.
├── requirements.txt # Python Dependencies
└── README.md # Project Documentation
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
or 
## Open a new terminal for activation of created python virtual environment
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

2. *Launch the UI (Open a new terminal and make sure the python virtual environment is activated.)*
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
 

> **Note:** In line with the assignment requirements, this project demonstrates a small agent design.  
> To keep the implementation lightweight, the agent currently consists of only a single node — the '*Summarize Node*'.  
>> API Key already provided for this assignment purpose. You can directly start using the agent without changing the API Key.

### *START → Summarize Node → END*

- Input JSON is passed to the summarize_host node.

- Gemini LLM generates a concise Markdown summary for each host.

- FastAPI returns the summary to the Streamlit UI for display.

## Future Improvements
- **Summary Modes**  
  Provide an option for the user to choose between:
  - *Quick Summary* (fast, high-level overview)  
  - *Detailed Analysis* (deeper insights with more computation)  

- **Flexible Input Options**  
  Allow users to either:  
  - Upload a `.json` file  
  - Paste raw JSON text directly into a text area  

- **Export & Downloads**  
  Enable users to download the generated summary in multiple formats:  
  - `.md` (Markdown)  
  - `.pdf`  
  - `.docx`  

- **Agent Enhancements**  
  Improve the summarization agent by:  
  - Adding new reasoning capabilities  
  - Creating domain-specific features tailored to Censys/host data  

- **Data Validation**  
  Validate the JSON input before sending it to the API, ensuring required keys and structure are present.  

- **Enhanced UI/UX**  
  - More user-friendly interface with collapsible sections  

- **Dataset Comparison**  
  Allow users to upload and analyze **two JSON datasets** side by side for comparison.  
