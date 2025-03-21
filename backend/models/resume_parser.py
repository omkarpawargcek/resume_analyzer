import re

def extract_email(text):
    match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    return match.group(0) if match else None

def extract_phone(text):
    match = re.search(r"\+?\d[\d -]{8,14}\d", text)
    return match.group(0) if match else None

def extract_education(text):
    degrees = ["B.Tech", "M.Tech", "B.E", "M.E", "B.Sc", "M.Sc", "PhD", "MBA"]
    education = [deg for deg in degrees if deg in text]
    return education if education else "Not Found"

def extract_experience(text):
    matches = re.findall(r"(\d{1,2})\s?(years|yrs|Months|months)", text)
    experience = sum(int(m[0]) for m in matches) if matches else "Not Found"
    return f"{experience} years" if experience != "Not Found" else experience

def extract_skills(text):
    common_skills = ["Python", "Java", "C++", "Machine Learning", "Data Science", "React", "Flask", "SQL"]
    skills_found = [skill for skill in common_skills if skill.lower() in text.lower()]
    return skills_found if skills_found else "Not Found"

def parse_resume(text):
    return {
        "email": extract_email(text),
        "phone": extract_phone(text),
        "education": extract_education(text),
        "experience": extract_experience(text),
        "skills": extract_skills(text),
    }
