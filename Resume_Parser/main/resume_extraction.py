# resume_extraction.py

import re

def extract_name(text):
    return text.split('\n')[0].strip()

def extract_contact_details(text):
    phone = re.findall(r'\b\d{10}\b', text)
    email = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    github = re.findall(r'\bhttps?://(?:www\.)?github\.com/[A-Za-z0-9._%+-]+\b', text)
    linkedin = re.findall(r'\bhttps?://(?:www\.)?linkedin\.com/[A-Za-z0-9-_/]+\b', text)

    return {
        "Phone": phone[0] if phone else "N/A",
        "Email": email[0] if email else "N/A",
        "GitHub": github[0] if github else "N/A",
        "LinkedIn": linkedin[0] if linkedin else "N/A",
    }


def extract_education(text):
    hsc_pattern = r'NMC Matriculation Higher Secondary School.*?(\d{1,2}\.\d{1,2})%'
    sslc_pattern = r'SBKV Matriculation Higher Secondary School.*?(\d{1,2}\.\d{1,2})%'
    bachelors_pattern = r'\b(?:B\.\w+|B\w+|Bachelor\'s|Bachelors|Sri Eshwar College of Engineering)\b.*?CGPA:\s*(\d{1,2}\.\d{1,2})\*?'
    
    hsc_matches = re.findall(hsc_pattern, text, re.IGNORECASE)
    sslc_matches = re.findall(sslc_pattern, text, re.IGNORECASE)
    bachelors_matches = re.findall(bachelors_pattern, text, re.IGNORECASE)
    
    hsc_percentage = hsc_matches[0] if hsc_matches else "N/A"
    sslc_percentage = sslc_matches[0] if sslc_matches else "N/A"
    bachelors_cgpa = bachelors_matches[0] if bachelors_matches else "N/A"
    
    return {
        "HSC": hsc_percentage,
        "SSLC": sslc_percentage,
        "Bachelors": bachelors_cgpa,
        
    }




def extract_skills(text):
    skills_section = re.search(r'TECHNICAL SKILLS\s*([\s\S]*?)(?:\n\n|\bEDUCATIONAL QUALIFICATION\b|\bEXPERIENCE\b|$)', text, re.IGNORECASE)
    if skills_section:
        skills_text = skills_section.group(1).strip()
        skills_lines = skills_text.split('\n')
        skills_list = []
        for line in skills_lines:
            skills_list.extend(line.split(', '))
        return {
            "Skills": [skill.strip() for skill in skills_list if skill.strip()]
        }
    return {"Skills": []}

def extract_experience(text):
    experience_sections = re.findall(r'Experience\s*:\s*([\s\S]*?)(?=\n\n|\Z)', text, re.IGNORECASE)
    if experience_sections:
        experiences = experience_sections[0].strip().split('\n')
        formatted_experiences = [" ".join(exp.strip().split()) for exp in experiences if exp.strip()]
        return formatted_experiences
    return ["N/A"]

def summarize_resume(text):
    return {
        "Name": extract_name(text),
        "Contact Details": extract_contact_details(text),
        "Education Details": extract_education(text),
        "Skills": extract_skills(text),
        "Experience": extract_experience(text),
    }




