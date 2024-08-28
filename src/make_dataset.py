import PyPDF2

def pdf_to_text(pdf_path, txt_path):
    # Open the PDF file
    with open(pdf_path, 'rb') as pdf_file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        
        # Initialize a variable to hold the extracted text
        extracted_text = ""
        
        # Iterate through each page and extract text
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            extracted_text += page.extract_text()
        
        # Write the extracted text to a text file
        with open(txt_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(extracted_text)

if __name__ == '__main__':
    # Specify the paths for the input PDF and output text file
    pdf_path = './data/raw/input.pdf'  # Replace with your PDF file path
    txt_path = './data/processed/output.txt'  # Replace with your desired output text file path

    # Call the function to convert PDF to text
    pdf_to_text(pdf_path, txt_path)