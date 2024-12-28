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
Refer to main.py


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
