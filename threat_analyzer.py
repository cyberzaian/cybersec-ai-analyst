import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def analyze_log_entry(entry):
    prompt = f"""
You are an expert cybersecurity analyst. Review the log and identify:
- Threat type (e.g., brute force, SQL injection)
- Severity level (low, medium, high)
- Response recommendation

Log:
{entry}
    """
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print("❌ Gemini API Error:", e)
        return f"❌ Gemini API Error: {e}"
