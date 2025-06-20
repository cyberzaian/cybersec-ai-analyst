from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_log_entry(entry):
    print("DEBUG ENTRY:", entry)

    prompt = f"""
You are an expert cybersecurity analyst. Review the log and identify:
- Threat type (e.g., brute force, SQL injection)
- Severity level (low, medium, high)
- Response recommendation

Log:
{entry}
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        print("DEBUG RESPONSE:", response)
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("ERROR during OpenAI call:", e)
        return "❌ Failed to analyze log entry. Check console logs or API key."
