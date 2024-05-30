


# resume_formatting.py

def format_resume_summary(resume_summary):
    # Format Contact Details with commas
    contact_details = (
        f"Phone: {resume_summary['Contact Details']['Phone']}, "
        f"Email: {resume_summary['Contact Details']['Email']}, "
        f"GitHub: {resume_summary['Contact Details']['GitHub']}, "
        f"LinkedIn: {resume_summary['Contact Details']['LinkedIn']}"
    )

    # Format Education Details
    education_details = (
        f"HSC: {resume_summary['Education Details']['HSC']}\n"
        f"SSLC: {resume_summary['Education Details']['SSLC']}\n"
        f"Bachelors: {resume_summary['Education Details']['Bachelors']}\n"
        f"Masters: {resume_summary['Education Details']['Masters']}"
    )

    # Join skills into a string separated by new lines
    skills = "\n".join(resume_summary["Skills"]["Skills"])

    # Join experience into a string separated by new lines
    experience = "\n".join(resume_summary["Experience"])

    # Format the entire summary with proper spacing
    formatted_summary = (
        f"Name: {resume_summary['Name']}\n\n"
        f"Contact Details: {contact_details}\n\n"
        f"Education Details:\n{education_details}\n\n"
        f"Skills:\n{skills}\n\n"
        f"Experience:\n{experience}"
    )

    return formatted_summary
