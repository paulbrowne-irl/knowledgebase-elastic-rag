

'''
Extract targetted information from PDF

'''
from tempfile import TemporaryDirectory
from pathlib import Path

import pytesseract
from pdf2image import convert_from_path
from PIL import Image


import logging

import re
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE


from PyPDF2 import PdfReader




def extract_text_info_with_ocr(filename: str) -> str:
    '''
    Loop through and extract key information from the document as text - assumes not image
    Based on - https://www.geeksforgeeks.org/python-reading-contents-of-pdf-using-ocr-optical-character-recognition/
    '''
    # Path of the Input pdf
    PDF_file = Path(filename)

    # Store all the pages of the PDF in a variable
    image_file_list = []

    pdf_text = ""

    # creating a pdf reader object
    reader = PdfReader(filename)

    with TemporaryDirectory() as tempdir:

        # Part #1 : Converting PDF to images
		
        # Read in the PDF file at 500 DPI
        pdf_pages = convert_from_path(PDF_file, 500)

        # Create a temporary directory to hold our temporary images.   
		# Iterate through all the pages stored above
        for page_enumeration, page in enumerate(pdf_pages, start=1):
			# enumerate() "counts" the pages for us.

			# Create a file name to store the image
            filename = f"{tempdir}\page_{page_enumeration:03}.jpg"
            logging.info("Storing tmp image:"+filename)

			# Declaring filename for each page of PDF as JPG
			# For each page, filename will be:
			# PDF page 1 -> page_001.jpg
			# PDF page 2 -> page_002.jpg
			# PDF page 3 -> page_003.jpg
			# ....
			# PDF page n -> page_00n.jpg

			# Save the image of the page in system
            page.save(filename, "JPEG")
            image_file_list.append(filename)

        """
        Part #2 - Recognizing text from the images using OCR
        """

        # Open the file in append mode so that
        # All contents of all images are added to the same file

        # Iterate from 1 to total number of pages
        for image_file in image_file_list:

            # Set filename to recognize text from
            # Again, these files will be:
            # page_1.jpg
            # page_2.jpg
            # ....
            # page_n.jpg

            # Recognize the text as string in image using pytesserct
            text = str(((pytesseract.image_to_string(Image.open(image_file)))))

            #make xl safe
            text=ILLEGAL_CHARACTERS_RE.sub(r'',text)

            # The recognized text is stored in variable text
            # Any string processing may be applied on text
            # Here, basic formatting has been done:
            # In many PDFs, at line ending, if a word can't
            # be written fully, a 'hyphen' is added.
            # The rest of the word is written in the next line
            # Eg: This is a sample text this word here GeeksF-
            # orGeeks is half on first line, remaining on next.
            # To remove this, we replace every '-\n' to ''.
            text = text.replace("-\n", "")

            # Finally, append the processed text to main output
            #logger.info("Ocr extracted text:"+text)
            pdf_text+=text

        return pdf_text





def extract_text_info_no_ocr(filename: str) -> str:
    '''
    Loop through and extract key information from the document as text - assumes not image
    '''

    pdf_text = ""

    # creating a pdf reader object
    reader = PdfReader(filename)

    # get all the text from the pdf file
    for i in range(len(reader.pages)):
        page = reader.pages[i]

        logging.debug("Extracting text from pdf page:"+str(i))

        # extracting text from page
        pdf_text += page.extract_text()

    # remove special charaters
    pdf_text = re.sub("[|'’€$@%–&•*/]", "", pdf_text)

    return pdf_text

