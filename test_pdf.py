# test_pdf.py
from pdf_utils import extract_text_from_pdf

pdf_path = "sample.pdf"  # or "test_files/sample.pdf"
text = extract_text_from_pdf(pdf_path)

print("Extracted Text Preview:\n")
print(text[:1000])  # Print first 1000 characters

