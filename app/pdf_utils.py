from pypdf import PdfReader


def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)#deepali.pdf
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text
