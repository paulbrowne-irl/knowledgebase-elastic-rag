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


# Prompt
TEMPLATE_QA_PROMPT = """
I am a helpful AI that answers questions. When I don't know the answer I say I don't know.
I know context: {context}
when asked: {question}
my response using only information in the context is: """

TEMPLATE_EMAIL_PROMPT = """
I am a helpful AI that writes 5 line emails as best I can in a professional tone.
I know context: {context}
when asked: {question}
my response is 5 lines long and begins with 'Dear Sir' and ends with 'regards, Bot'
"""


######
# System level properties

# Most of the time you will not need to edit these settings
LOG_FILE="app.log"

#####
# possible to remove these

#Constants - SW Sample
#index_name = "book_wookieepedia_small"
#topic = "Star Wars"


###=====
### EMAIL settings - remove
#####

# Settings that configure how the script behaves
# The most common ones to edit are below

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



