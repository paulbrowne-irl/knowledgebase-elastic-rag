

'''
Simple script to extract targetted information from PDF

'''
from tempfile import TemporaryDirectory
from pathlib import Path

import pytesseract
from pdf2image import convert_from_path
from PIL import Image

import docx2txt

import logging
import os
import os.path

import re
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE

import pandas as pd
from pandas.core.frame import DataFrame
from PyPDF2 import PdfReader

import settings


INPUT_DIR = "confidential-data"
OUTPUT_DIR = "confidential-output"


def _loop_extract_text_info_word(filename: str) -> str:
    text = docx2txt.process(filename)

    return text

def _loop_extract_text_info_with_ocr(filename: str) -> str:
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
            logger.info("Storing tmp image:"+filename)

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





def _loop_extract_text_info_no_ocr(filename: str) -> str:
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


# Loop code to run from command line
if __name__ == '__main__':

    # setup logging
    logger = logging.getLogger("")
    logger.setLevel(logging.DEBUG)

    # for testing - break after x goes
    counter = 0

    # create output dataframe
    output_df = pd.DataFrame([], columns=[
                             'Case', 'Size','Text'])

    # iterate over files in directory
    for filename in os.listdir(INPUT_DIR):

        #reset document text
        document_text=""

        try:

            if filename.lower().endswith(".pdf"):

                logging.info("processing pdf file: "+filename)

                # Get the next file in this directory
                f = os.path.join(INPUT_DIR, filename)

                # Extract information using two methodologies
                document_text = _loop_extract_text_info_no_ocr(f)
                document_text= document_text+_loop_extract_text_info_with_ocr(f)

                #logging.info("Extracted Text:"+document_text)

            elif filename.lower().endswith(".docx"):
                logging.info("processing word file: "+filename)

                # Get the next file in this directory
                f = os.path.join(INPUT_DIR, filename)

                # Extract _extract_text_stats information
                document_text = _loop_extract_text_info_word(f)
            else:
                logging.info("non recognized format: "+filename)
                document_text = "unable to extract transfer reason"


            # break if this is set
            counter += 1
            if counter >= settings.MAX_NUMBER_OF_FILES:
                logger.warning("ENDING AFTER MAX 7CYCLE:")
                break

        except Exception as problem:

            # decide how to handle it
            if (settings.CONTIUE_LOOP_AFTER_ERROR):
                # Log the error and continue loop
                logging.error(problem)

            else:
                # rethrow the error and end
                raise problem
        
        finally:
            # add this as new row to output
            new_record = pd.DataFrame([{'Case':filename, 'Size':len(document_text), 'Text':document_text}])
            output_df = pd.concat([output_df, new_record], ignore_index=True)
            logger.info("Added:"+str(counter)+" :"+filename+" :length "+str(len(document_text)))
            logger.info("=================================================/n")

            output_df.to_excel(settings.OUTPUT_TEXT_ANALSYIS, index=False)

        

    # export information into the folder as Excel
    logging.info("Exporting to file:"+settings.OUTPUT_TEXT_ANALSYIS)
    output_df.to_excel(settings.OUTPUT_TEXT_ANALSYIS, index=False)
