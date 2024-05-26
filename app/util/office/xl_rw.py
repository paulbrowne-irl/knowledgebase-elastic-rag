import logging

import pandas as pd


'''
Util file to read and write excel file
'''

def has_unaswered_question(xl_file_name:str,answer_col:str)->bool:

        
    #root_folder = .Folders.Item(1)
    logging.debug("Getting handle to Excel with Emails");
    question_table = pd.read_excel(xl_file_name, index_col=0)

    logging.info("Filtering based on unanswered questions in:"+answer_col) 

    # filter based on answered question
    filtered_table = question_table[question_table[answer_col].isnull()]

    #close file

    # return 
    return len(filtered_table.index)>0




def read_next_unanswered_question(xl_file_name:str,question_col:str,answer_col:str)->pd.DataFrame:

    '''read values from xl file
    Keyword Arguments:
    xl_file_name -- to read the questions from
    question_col -- the name of the column in excel that the next question will be read from
    answer_col -- used to filter to see what has been answered (or not)
    return - 1 line of a pandas dataframe
    '''
    
    #root_folder = .Folders.Item(1)
    logging.debug("Getting handle to Excel with Emails");
    question_table = pd.read_excel(xl_file_name, index_col=0)

    logging.info("Filtering based on unanswered questions in:"+answer_col) 

    # filter based on answered question
    filtered_table = question_table[question_table[answer_col].isnull()]

    #return only the first row of this filtered table
    return filtered_table.iloc[0]

