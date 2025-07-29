# PDF Merge Tool

A simple Python utility to automatically find and merge all PDF files in a specified folder into a single PDF document.

## Features

- Automatically discovers all PDF files in a folder (including subfolders)
- Merges PDFs in the order they are found
- Simple configuration through path variables
- Preserves original files while creating a merged output

## Requirements

- Python 3.x
- PyPDF2 library

## Installation

1. Install the required dependency:
```bash
pip install PyPDF2
```

2. Download or clone this repository

## Usage

1. Open `pd_merge_auto.py` in a text editor

2. Update the folder path to point to your PDF directory:
```python
folder_path = r"C:\Users\your_username\path\to\pdf\folder"
```

3. Set your desired output file path and name:
```python
output_file = r"C:\Users\your_username\path\to\output\merged_file.pdf"
```

4. Run the script:
```bash
python pd_merge_auto.py
```

## How It Works

The tool performs three main operations:

1. **PDF Discovery**: Recursively searches the specified folder and all subfolders for PDF files
2. **File Collection**: Builds a list of all PDF file paths found
3. **Merging**: Combines all PDFs into a single output file using PyPDF2

## Functions

- `find_pdfs(folder_path)`: Recursively finds all PDF files in the specified directory
- `merge_PDFs(paths, output)`: Takes a list of PDF file paths and merges them into a single output file

## Notes

- PDFs are merged in the order they are discovered by the file system
- The script will overwrite any existing file at the output path
- Ensure you have write permissions for the output directory
- Large numbers of PDFs or very large PDF files may take some time to process

## Example

If you have a folder structure like:
```
Documents/
├── report1.pdf
├── report2.pdf
└── subfolder/
    └── report3.pdf
```

The tool will find and merge all three PDFs into your specified output file.

## Troubleshooting

- **Import Error**: Make sure PyPDF2 is installed (`pip install PyPDF2`)
- **File Not Found**: Check that your folder path exists and contains PDF files
- **Permission Error**: Ensure you have read access to the source folder and write access to the output location
- **Path Issues**: Use raw strings (prefix with `r`) for Windows paths to handle backslashes correctly
