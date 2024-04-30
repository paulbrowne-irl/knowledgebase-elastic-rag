import logging
import traceback
from pandas.core.frame import DataFrame


import pandas as pd


import app.settings.config as config

'''
Util file to read and write excel file
'''

def read_xl(xl_file_name):

    '''read values from xl file'''
    
    #root_folder = .Folders.Item(1)
    print("Getting handle to Excel with Emails");
    email_table = pd.read_excel(xl_file_name, index_col=0) 

    return email_table

