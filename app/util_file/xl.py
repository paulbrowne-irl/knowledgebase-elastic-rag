import logging
import traceback
from pandas.core.frame import DataFrame


import pandas as pd


'''
Util file to read and write excel file
'''

def read_next_unanswered_question(xl_file_name):

    '''read values from xl file'''
    
    #root_folder = .Folders.Item(1)
    print("Getting handle to Excel with Emails");
    question_table = pd.read_excel(xl_file_name, index_col=0) 

    # filter based on answered question
    filtered_table = question_table[question_table['Answer'].isnull()]

    #return only the first row of this filtered table
    return filtered_table.iloc[0]

