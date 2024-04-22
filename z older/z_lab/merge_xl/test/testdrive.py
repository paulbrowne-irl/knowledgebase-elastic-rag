
import logging
import os

import pandas as pd

import testsettings

# allow imports from parent directory
import sys
sys.path.append('../project_xl')
import collate

#setup logging
logger = logging.getLogger("")
logger.setLevel(logging.DEBUG)

#Open the two dataframes
main_df=pd.read_excel(testsettings.TEST_DF_CHECKLIST)
add_df=pd.read_excel(testsettings.TEST_DF_2)

#Combine
merged_df= collate._merge_dataframes(main_df,add_df)
merged_df.to_excel(testsettings.TEST_OUTPUT)