from PyPDF2 import PdfFileMerger

pdf_files = ['sample_page1.pdf', 'pdf_files/sample_page2.pdf']

with PdfFileMerger() as merger:
    [merger.append(pdf_file) for pdf_file in pdf_files]
    merger.write("merged_2_pages.pdf")
