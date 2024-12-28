import pytesseract
from pdf2image import convert_from_path
import os

def extract_text_with_ocr(pdf_path, txt_output_path, tesseract_cmd=None):
    try:
        # Optionally set the Tesseract-OCR executable path
        if tesseract_cmd:
            pytesseract.pytesseract.tesseract_cmd = tesseract_cmd

        # Convert PDF pages to images
        images = convert_from_path(pdf_path)

        # Initialize a string to store the extracted text
        extracted_text = ""

        # Loop through each image and extract text using OCR
        for page_num, image in enumerate(images):
            extracted_text += pytesseract.image_to_string(image, lang='eng')

        # Process the extracted text
        paragraphs = extracted_text.split("\n\n")
        final_output = []

        for paragraph in paragraphs:
            if paragraph.startswith("ALJ") or paragraph.startswith("ATTY") or paragraph.startswith("CLMT"):
                final_output.append(" ".join(paragraph.splitlines()))

        # Write the processed text to a .txt file
        with open(txt_output_path, 'w', encoding='utf-8') as txt_file:
            for line in final_output:
                txt_file.write(line + "\n")

        print(f"Text successfully written to {txt_output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Process multiple PDF files
def process_multiple_pdfs(pdf_folder, output_folder, tesseract_cmd=None):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(pdf_folder):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(pdf_folder, filename)
            txt_output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.txt")
            print(f"Processing {filename}...")
            extract_text_with_ocr(pdf_path, txt_output_path, tesseract_cmd)

pdf_folder = 'test'  
output_folder = 'output_folder'  
tesseract_cmd = '/opt/homebrew/bin/tesseract'

# Call the function to process multiple PDFs
process_multiple_pdfs(pdf_folder, output_folder, tesseract_cmd)
