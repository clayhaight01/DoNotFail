import fitz

def pdf2png(pdf_path, output_folder):
    pdf_document = fitz.open(pdf_path)

    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)

        image = page.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), alpha=False)
        image.save(f"{output_folder}/page_{page_num + 1}.png")

    pdf_document.close()
