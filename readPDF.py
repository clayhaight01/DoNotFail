import PyPDF2

def readPDF(filename):
    with open(filename, 'rb') as file:
        # Initialize a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)
        
        text = ''
        # Loop through all the pages in the PDF (if there are multiple)
        for index, page in enumerate(pdf_reader.pages):
            text += f"Page {index+1}\n"
            text += "=" * 40
            text += "\n"
            text += page.extract_text()
        
        return text
