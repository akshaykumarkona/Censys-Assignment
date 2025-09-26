import streamlit as st
import requests
import json
from summarizer import agent

# Change if your backend runs elsewhere
API_URL = "http://localhost:8000/summarize"

st.set_page_config(page_title="Host Dataset Summarizer")
st.title("Censys Host Dataset Summarizer")

st.markdown(
    "Upload a Censys-style JSON file. "
    "The app will send the entire dataset to the backend which forwards it to the LangGraph agent."
)

input_data = None  


uploaded = st.file_uploader(
    "Drag & drop or select a JSON file",
    type=["json"],
    accept_multiple_files=False
)

if uploaded:
    try:
        # Parse JSON
        input_data = json.load(uploaded)

        # Success message with details
        st.success(f"File **{uploaded.name}** loaded successfully")
        st.caption(f"File size: {uploaded.size / 1024:.2f} KB")

        # Show JSON preview
        with st.expander("👀 Preview JSON content (first 1000 chars)"):
            preview = json.dumps(input_data, indent=2)[:1000]
            st.code(preview, language="json")

    except Exception as e:
        st.error(f"Error parsing uploaded file: {e}")



# Send to backend
if input_data is not None:
    if st.button("Generate Summary for Dataset"):
        with st.spinner("Please wait, Summarizing dataset...😊"):
            try:
                resp = requests.post(API_URL, json=input_data, timeout=120)
                if resp.status_code == 200:
                    payload = resp.json()
                    # Backend returns {"summary": "..."} per your latest spec
                    summary = payload.get("summary") or payload.get("summaries") or ""
                    if isinstance(summary, str):
                        st.subheader("Dataset Summary")
                        st.markdown(summary)
                    else:
                        # fallback if backend returns other structure
                        # st.write(payload)
                        st.write("HI")
                        # import json
                        # st.markdown("```json\n" + json.dumps(payload, indent=2) + "\n```")

                else:
                    st.error(f"Backend error {resp.status_code}: {resp.text}")
            except requests.exceptions.RequestException as err:
                st.error(f"Request failed: {err}")
