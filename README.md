# OCR Text Extraction with PyTesseract and MuPDF

This repository demonstrates a Python-based solution for Optical Character Recognition (OCR) to extract text from PDF files that may not be machine-readable and convert them into plain text files. The project uses the `pytesseract` library for OCR and `mupdf` for PDF file handling.

## Features
- Extract text from PDFs with non-selectable text using OCR.
- Convert images or scanned PDF pages to readable text.
- Save the extracted text into `.txt` files for easy access and usage.

## Requirements

### Prerequisites
Ensure you have the following installed on your system:
- Python 3.7+
- Tesseract-OCR

### Python Libraries
Install the required Python libraries using pip:

```bash
pip install pytesseract mupdf
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ocr-text-extraction.git
   cd ocr-text-extraction
   ```
2. Ensure `tesseract` is installed and available in your PATH.
   - For Windows: [Download Tesseract-OCR](https://github.com/tesseract-ocr/tesseract)
   - For macOS: Install via Homebrew:
     ```bash
     brew install tesseract
     ```
   - For Linux: Install via your package manager:
     ```bash
     sudo apt-get install tesseract-ocr
     ```

## Usage

1. Place the PDF files you want to process into the `input_pdfs/` directory.
2. Run the script:

   ```bash
   python ocr_extraction.py
   ```
3. The extracted text files will be saved in the `output_txt/` directory with the same base name as the input PDF.

## Code Example
Here is the main script for processing PDF files:

```python
import os
import pytesseract
import fitz  # MuPDF

# Directories
input_dir = "input_pdfs"
output_dir = "output_txt"
os.makedirs(output_dir, exist_ok=True)

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file using OCR."""
    with fitz.open(pdf_path) as pdf:
        text = ""
        for page_num, page in enumerate(pdf):
            pix = page.get_pixmap()  # Render page to an image
            image_path = f"temp_page_{page_num}.png"
            pix.save(image_path)

            # Perform OCR on the image
            text += pytesseract.image_to_string(image_path) + "\n"

            # Cleanup temporary image
            os.remove(image_path)

        return text

def process_pdfs():
    """Process all PDFs in the input directory."""
    for file_name in os.listdir(input_dir):
        if file_name.lower().endswith(".pdf"):
            pdf_path = os.path.join(input_dir, file_name)
            print(f"Processing {file_name}...")

            text = extract_text_from_pdf(pdf_path)

            # Save extracted text to a .txt file
            output_path = os.path.join(output_dir, file_name.replace(".pdf", ".txt"))
            with open(output_path, "w", encoding="utf-8") as text_file:
                text_file.write(text)

            print(f"Saved extracted text to {output_path}")

if __name__ == "__main__":
    process_pdfs()
```

## Directory Structure
```
.
├── input_pdfs/        # Place your PDF files here
├── output_txt/        # Extracted text files will be saved here
├── ocr_extraction.py  # Main script for processing
└── README.md          # Project documentation
```

## Contributing
Contributions are welcome! Please fork this repository and submit a pull request for any improvements or new features.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [PyTesseract](https://pypi.org/project/pytesseract/) for OCR capabilities.
- [MuPDF](https://pymupdf.readthedocs.io/) for efficient PDF rendering.
