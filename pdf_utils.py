# pdf_utils.py
import fitz  # PyMuPDF

def extract_text_from_pdf(file_path: str) -> str:
    """Extracts and returns all text from a PDF file."""
    try:
        doc = fitz.open(file_path)
        full_text = ""

        for page in doc:
            full_text += page.get_text()
        
        doc.close()
        return full_text

    except Exception as e:
        return f"Error reading PDF: {str(e)}"
