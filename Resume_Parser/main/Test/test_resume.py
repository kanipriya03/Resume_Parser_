import sys
import os
import pytest

# Ensure the parent directory of the 'main' module is in the PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from main.resume_extraction import extract_name, extract_contact_details, extract_education, extract_skills, extract_experience,summarize_resume

# Test case for extract_name
def test_extract_name():
    text = "Jane Doe"
    assert extract_name(text) == "Jane Doe"
# Name not found
    text = ""
    assert extract_name(text) == ""


# Test case for extract_contact_details
def test_extract_contact_details():
    text = "Phone: 1234567890\nEmail: john.doe@example.com\nGitHub: https://github.com/johndoe\nLinkedIn: https://linkedin.com/in/johndoe"
    expected_output = {
        "Phone": "1234567890",
        "Email": "john.doe@example.com",
        "GitHub": "https://github.com/johndoe",
        "LinkedIn": "https://linkedin.com/in/johndoe"
    }
    assert extract_contact_details(text) == expected_output

    text = "Phone: 0987654321\nEmail: jane.doe@example.com"
    expected_output = {
        "Phone": "0987654321",
        "Email": "jane.doe@example.com",
        "GitHub": "N/A",
        "LinkedIn": "N/A"
    }
    assert extract_contact_details(text) == expected_output
# No contact details
    text = "No contact details here."
    expected_output = {
        "Phone": "N/A",
        "Email": "N/A",
        "GitHub": "N/A",
        "LinkedIn": "N/A"
    }
    assert extract_contact_details(text) == expected_output

# Test case for extract_education
def test_extract_education():
    text = """
    Higher Secondary School Certificate (2010-2012)
    Some details here
    Percentage: 95.5%

    B.E Computer Science Engineering (2012-2016)
    Some details here
    CGPA: 8.5
    """
    expected_output = {
        "Bachelors": "N/A",
        "HSC": "N/A",
        "SSLC": "N/A",
        
        
    }
    assert extract_education(text) == expected_output

    text = """
    Secondary School Leaving Certificate (2008-2010)
    Some details here
    Percentage: 90.0%

    M.Tech Computer Science Engineering (2016-2018)
    Some details here
    CGPA: 9.0
    """
    expected_output = {
        "Bachelors": "N/A",
        "HSC": "N/A",
        "SSLC": "N/A",
        
        
    }
    assert extract_education(text) == expected_output
# No education details
    text = "No education details here."
    expected_output = {
        "Bachelors": "N/A",
        "HSC": "N/A",
        "SSLC": "N/A",
       
        
    }
    assert extract_education(text) == expected_output

# Test case for extract_skills
def test_extract_skills():
    text = """
    TECHNICAL SKILLS
    Python, Java, C++, Communication, Leadership
    """
    expected_output = {
        "Skills": ['Python', 'Java', 'C++', 'Communication', 'Leadership']
    }
    assert extract_skills(text) == expected_output

    text = "No skills listed here."
    expected_output = {
        "Skills": []
    }
    assert extract_skills(text) == expected_output

# Test case for extract_experience
def test_extract_experience():
    text = """
    Experience:
    Company A: Software Developer Responsibilities...
    Company B: Intern Responsibilities...
    """
    expected_output = [
        "Company A: Software Developer Responsibilities...",
        "Company B: Intern Responsibilities..."
    ]
    assert extract_experience(text) == expected_output

    text = "No experience listed here."
    expected_output = ["N/A"]
    assert extract_experience(text) == expected_output





