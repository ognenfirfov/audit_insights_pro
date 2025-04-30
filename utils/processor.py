from openai import OpenAI
import fitz  # PyMuPDF
import os

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_text(pdf_path):
    """Extract text from a PDF file using PyMuPDF."""
    doc = fitz.open(pdf_path)
    return "\n".join(page.get_text() for page in doc)

def summarize_audit(text):
    """Summarize key elements of a single audit using AI."""
    prompt = f"""You are an auditor. Analyze the following audit report and summarize:
- Key Findings
- Measures Taken
- Key Issues
- Notable Outcomes

Report:
{text}

Return a clear, bullet-point or structured summary.
"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user]()
