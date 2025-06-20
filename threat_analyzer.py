from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_log_entry(entry):
    prompt = f"""
You are an expert cybersecurity analyst. Review the log and identify:
- Threat type (e.g., brute force, SQL injection)
- Severity level (low, medium, high)
- Response recommendation

Log:
{entry}
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
