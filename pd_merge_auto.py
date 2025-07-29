import os
from PyPDF2 import PdfMerger


# Function that will loop through the pdf_files list and merge each
# PDF until there are no longer any file addresses in the list remaining
def merge_PDFs(paths, output):
    merger = PdfMerger()

    for path in paths:
        merger.append(path)

    merger.write(output)
    merger.close()

# Function to find all PDFs in a given folder
def find_pdfs(folder_path):
    pdf_files =[]
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.pdf'):
                pdf_files.append(os.path.join(root, file))
    return pdf_files

# Variable to store the path to the folder containing PDFs
folder_path = r"C:\Users\dominguezj\Documents\APV\Mainstay\vacancy\Jane-June"

# Finds all PDFs in the specified folder
pdf_files = find_pdfs(folder_path)

# Here is a variable holding the location of where we will save the output file
output_file = r"C:\Users\dominguezj\Documents\APV\Mainstay\vacancy\Jane-June\APV_Mainstay_Vacnacy_2025.pdf"

# we will now feed our list of PDFs and their respective locations into 
# the function. We will also feed where to save the merged PDF.
merge_PDFs(pdf_files, output_file)