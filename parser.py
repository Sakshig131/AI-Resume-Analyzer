import pdfplumber
import re


def clean_text(text):
    """
    Clean extracted resume text.
    """

    # Replace multiple spaces with single space
    text = re.sub(r"\s+", " ", text)

    # Remove unwanted characters
    text = text.replace("\n", " ")
    text = text.replace("\t", " ")

    return text.strip().lower()


def extract_text(file):
    """
    Extract text from uploaded PDF resume.
    """

    text = ""

    try:
        with pdfplumber.open(file) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + " "

    except Exception as e:

        return f"Error reading PDF: {e}"

    return clean_text(text)