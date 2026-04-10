from llm import call_llm

def analyze_resume(text, job_desc):
    prompt = f"""
Analyze resume vs job description.

Give:
- Strengths
- Weaknesses
- Missing Skills
- ATS Score (0-100)
- Job Match %

Resume:
{text}

Job Description:
{job_desc}
"""
    return call_llm(prompt)
