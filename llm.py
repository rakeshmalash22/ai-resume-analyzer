def call_llm(prompt):
    text = prompt.lower()

    strengths = []
    weaknesses = []
    missing_skills = []

    # Strength detection
    if "python" in text:
        strengths.append("Strong Python skills")
    if "machine learning" in text:
        strengths.append("Good ML knowledge")
    if "sql" in text:
        strengths.append("Database knowledge")
    if "project" in text:
        strengths.append("Hands-on project experience")

    # Weakness detection
    if "deep learning" not in text:
        weaknesses.append("No Deep Learning mentioned")
        missing_skills.append("Deep Learning")
    if "nlp" not in text:
        weaknesses.append("No NLP experience")
        missing_skills.append("NLP")
    if "deployment" not in text:
        weaknesses.append("No deployment experience")
        missing_skills.append("Model Deployment")

    # ATS Score logic
    score = 50 + (len(strengths) * 10) - (len(weaknesses) * 5)
    score = max(0, min(100, score))

    result = f"""
🔍 Resume Analysis

✅ Strengths:
{chr(10).join(strengths) if strengths else "Basic profile"}

❌ Weaknesses:
{chr(10).join(weaknesses) if weaknesses else "None"}

📉 Missing Skills:
{chr(10).join(missing_skills) if missing_skills else "None"}

📊 ATS Score: {score}/100
"""

    return result
