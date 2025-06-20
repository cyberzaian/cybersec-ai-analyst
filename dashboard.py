import streamlit as st
from log_parser import parse_logs
from agents.planner_agent import plan_task
from agents.intelligence_agent import execute_analysis
from agents.responder_agent import respond_if_needed

st.set_page_config(page_title="AI Cybersecurity Analyst", layout="wide")
st.title("🛡️ AI-Powered Cybersecurity Analyst Dashboard")

uploaded_file = st.file_uploader("Upload a log file", type=["log", "txt"])
if uploaded_file:
    st.success("Log file uploaded successfully.")
    with open("uploaded.log", "wb") as f:
        f.write(uploaded_file.getbuffer())

    logs = parse_logs("uploaded.log")
    for log in logs:
        with st.expander(f"📄 {log['line']}"):
            task = plan_task(log["line"])
            analysis = execute_analysis(log["line"])
            response = respond_if_needed(log["ip"], analysis)

            st.markdown(f"**Plan:** `{task}`")
            st.markdown(f"""**Analysis:**  
