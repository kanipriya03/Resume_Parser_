# app.py
from resume_formatting import format_resume_summary
import streamlit as st
from resume_conversion import extract_text_from_pdf
from resume_extraction import (
    extract_name,
    extract_contact_details,
    extract_education,
    extract_skills,
    extract_experience,
)

def main():
    st.title("Resume Parser")

    uploaded_file = st.file_uploader("Upload a PDF resume", type="pdf")

    if uploaded_file is not None:
        resume_text = extract_text_from_pdf(uploaded_file)
        resume_summary = {
            "Name": extract_name(resume_text),
            "Contact Details": extract_contact_details(resume_text),
            "Education Details": extract_education(resume_text),
            "Skills": extract_skills(resume_text),
            "Experience": extract_experience(resume_text),
        }

        formatted_summary = format_resume_summary(resume_summary)
        st.subheader("Resume Summary:")
        st.markdown(formatted_summary)

if __name__ == "__main__":
    main()
