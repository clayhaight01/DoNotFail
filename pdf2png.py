import fitz  # PyMuPDF

def convert_pdf_to_png(pdf_path, output_folder):
    # Load the PDF
    pdf_document = fitz.open(pdf_path)

    # Iterate through each page in the PDF
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)

        # Render the page as a PNG image
        image = page.get_pixmap()

        # Save the image to the output folder
        image.save(f"{output_folder}/page_{page_num + 1}.png")

    # Close the PDF
    pdf_document.close()

# Example usage
convert_pdf_to_png('assignment.pdf', 'assignment_png')
