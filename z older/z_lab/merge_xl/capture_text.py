import logging
import os
import os.path
import pprint
import re
from collections import Counter
from pprint import pprint

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

import pandas as pd
from pandas.core.frame import DataFrame
from PyPDF2 import PdfReader

import settings.default

import util.file_export as file_export
import util.file_util as file_util



def _extract_text_stats(source_file_name,df_to_append_to,document):
    '''
    Extract Sentiment and keywords driving sentiment from document
    '''

    #needed first time, can comment out later (but check is fast)
    #nltk.download('vader_lexicon')

    #handle to the sentiment analyser
    sia = SentimentIntensityAnalyzer()

    #Break our text block into sentences    
    sentences = nltk.sent_tokenize(document)
    

    #Loop through the s
    for sent in sentences:
        
        #Get the sentiment
        sentiment = sia.polarity_scores(sent)

        #Get the keywords driving this sentiment
        sent_tokenized = nltk.word_tokenize(sent) 
        sent_pos_tagged = nltk.pos_tag(sent_tokenized) 

        # extract kewords (just NN and NNP pos, with keywords longer than 3 letters)
        keywords = [t[0] for t in sent_pos_tagged if (t[1] in ["NN","NNP"] and len(t[0])>3)]


        #Add to output dataframe if we have meaningful data to add
        if sentiment["compound"] !=0:
            new_row = {'Source': source_file_name, 
                    'Sentence': sent[:25]+" ...",
                    'Sentiment-Neg': sentiment["neg"], 
                    'Sentiment-Pos': sentiment["pos"], 
                    'Sentiment-Compound': sentiment["compound"],  
                    'Keywords': keywords}
            output_df.loc[len(output_df)] = new_row


    return output_df



def _loop_extract_text_info(filename:str)->pd.DataFrame:
    '''
    Loop through and extract key information from the tables in the document
    Operates on a company data object
    '''

    pdf_text=""

    # creating a pdf reader object
    reader = PdfReader(filename)
    
    
    # get all the text from the pdf file
    for i in range (len(reader.pages)):
        page = reader.pages[i]
    
        logging.debug("Extracting text from pdf page:"+str(i))

         # extracting text from page
        pdf_text += page.extract_text()
   
    #remove special charaters
    pdf_text=re.sub("[|'’€$@%–&•*/]","",pdf_text)

    return pdf_text
           
             

# Loop code to run from command line
if __name__ == '__main__':
    
    #setup logging
    logger = logging.getLogger("")
    logger.setLevel(logging.DEBUG)

    #for testing - break after x goes
    counter=0
  
    # create output dataframe
    output_df=  pd.DataFrame([], columns=['Source', 'Sentence','Sentiment-Neg','Sentiment-Pos','Sentiment-Compound','Keywords'])


    # iterate over files in directory
    for filename in os.listdir(settings.default.WORKING_FOLDER):
        
        try:

            if not filename.lower().endswith(".pdf"):
                logging.info("Ignoring non-pdf file: "+filename)
        
            else:

                logging.info("processing pdf file: "+filename)    

                #Get the next file in this directory
                f = os.path.join(settings.default.WORKING_FOLDER, filename)

                #Extract _extract_text_stats information
                document_text= _loop_extract_text_info(f)

                output_table = _extract_text_stats(filename,output_df,document_text)
 
                #break if this is set
                counter+=1
                if counter>=settings.default.MAX_NUMBER_OF_FILES:
                    logger.warning("ENDING AFTER CYCLE:"+str(settings.MAX_NUMBER_OF_FILES))
                    break
            

        except Exception as problem:


            #decide how to handle it
            if(settings.default.CONTIUE_LOOP_AFTER_ERROR):
                 #Log the error and continue loop
                logging.error(problem)
                
            else:
                #rethrow the error and end
                raise problem
            
    #export information into the folder as Excel
    logging.info("Exporting to file:"+settings.default.OUTPUT_TEXT_ANALSYIS)
    output_df.to_excel(settings.default.OUTPUT_TEXT_ANALSYIS,index=False)
