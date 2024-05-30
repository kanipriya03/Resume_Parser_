# Resume_Parser_

This project is a Resume Parser built using Python, Streamlit, and various libraries for text extraction and processing. The parser extracts key information from PDF resumes and displays it in a structured format on a web interface.

## Features

- Extracts name, contact details, education, skills, and experience from PDF resumes.
- Displays extracted information in a user-friendly format on a Streamlit web app.

## Prerequisites

- Python 3.12
- `pip` package manager
- Docker 

## Requirements 

This project uses the following libraries:
- `pdfminer.six` for PDF text extraction.
- `tabulate` for creating structured tables.
- `streamlit` for building the web interface.
- `pytest` and `pytest-cov` for testing and coverage reporting.

## Installation

1. **Set up a virtual environment :**
    
    python -m venv venv
    `venv\Scripts\activate`
   

2. **Install the required packages:**
  
    pip install -r requirements.txt


## Running the Application

1. **Run the Streamlit application:**

    streamlit run app.py
   

2. **Open your web browser and navigate to `http://localhost:8501` to access the app.**

## Directory Structure

- `app.py`: Main entry point for the Streamlit web app.
- `resume_formatting.py`: Contains the function to format the resume summary.
- `resume_conversion.py`: Contains the function to extract text from PDF resumes.
- `resume_extraction.py`: Contains functions to extract specific information from resume text.
- `requirements.txt`: Lists the required Python packages.
- `Dockerfile`: Defines the Docker image for the application.
- `tests/`: Directory containing test files for the project.

## Docker Setup

1. **Build the Docker image:**
    
    docker build -t resume-parser .
    

2. **Run the Docker container:**
    
    docker run -p 8501:8501 resume-parser
    
3. **Open your web browser and navigate to `http://localhost:8501` to access the app.**


## Testing with pytest and Coverage

To ensure the reliability of the resume parser, tests are implemented using `pytest`, a popular testing framework in Python. Additionally, `pytest-cov` is used to generate coverage reports, helping to gauge the extent of code coverage by tests.

### Running Tests

To run tests with `pytest`, follow these steps:

1. **Install pytest and pytest-cov:**
    pip install pytest pytest-cov

2. Run the tests:
    pytest
2. Run the pytest coverage:   
    coverage run -m pytest
