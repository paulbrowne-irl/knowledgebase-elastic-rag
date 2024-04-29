# Settings that configure how the script behaves
# The most common ones to edit are below

# Where we will output the results
# "." is the project home directory
WORKING_DIRECTORY="."

#Server
ES_URL = 'http://localhost:9200'

#Index names
ES_INDEX_DOCUMENTS = "knowledge-base"
ES_INDEX_FINANCIALS="sef-financials"
ES_INDEX_EMAILS = "emails"

#directories
#PDF_DIR = "../data-sample"
SOURCE_PDF_DIR="/mnt/c/Users/pbrowne/OneDrive - Enterprise Ireland/SEF Cases/"
SOURCE_MAILS_IN_XL="../data_no_share/data-emails.xlsx"

#Caching
CACHE_DIR = "../cache/"

# VECTOR Model
MODEL_TRANSFORMERS = "sentence-transformers/all-mpnet-base-v2"

# LLM Model
MODEL_LLM = 'google/flan-t5-large'



######
# System level properties

# Most of the time you will not need to edit these settings
LOG_FILE="app.log"

# Where we will output the results
# "." is the project home directory
WORKING_DIRECTORY="."



# The Name of the shared outlook inbox we want to walk 
INBOX_NAME="Business Response"
#INBOX_NAME="GA-BSF"


# Maximum number of emails that we will process
# Set to -1 if you want to process the entire folder
BREAK_AFTER_X_MAILS=-1

# Flush the cache to disk after X emails then continue
# It means we still have (most) information even if there is an error
FLUSH_AFTER_X_MAILS=100

#####

# Most of the time you will not need to edit these settings
LOG_FILE="email_ingest.log"



