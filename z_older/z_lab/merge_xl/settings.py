#
#Script Level settings
#
import pandas as pd

# the folder we will walk through
WORKING_FOLDER ="C:\\Users\\pbrowne\\Enterprise Ireland\\O'Donoghue, Anne - SEF Large Sample cases"
#WORKING_FOLDER="C:\\Users\\pbrowne\\OneDrive - Enterprise Ireland\\SEF Cases"

# a list of processed files that we will skip
PROCESSED_FILE_LIST="C:\\Users\\pbrowne\\Enterprise Ireland\\O'Donoghue, Anne - SEF Large Sample cases\Collate_processed_files.xlsx"

#The maximum number of files we will process
#for all files set to very high number e.g. 1000000
MAX_NUMBER_OF_FILES=500
 
#Attempt to continue after error - True for production, False for dev
CONTIUE_LOOP_AFTER_ERROR=True

#Lattice Mode - works better where the DA has copied pasted a graphic (instead of an Excel Table)
#But otherwise splits too many tables
#If we decect fewer than X tables (the number below) we will try again using lattice mode
LATTICE_THRESHOLD=10

# The name we will append to input file to get our output file anme
OUTPUT_APPEND= "_data.xlsx"

# The name we use when collating multiple sheets together
OUTPUT_COLLATE="Collate_d_"

# The name we use to export the text analysis
OUTPUT_TEXT_ANALSYIS="text_analysis.xlsx"

#the tab name we output Key info under
KEY_INFO_OUTPUT_TAB_NAME="Key Info"
KEY_WORDS_OUTPUT_TAB_NAME="Keywords"

#Key info that we search for and pull out of tables
KEY_INFO_SEARCH=["Sustaining Enterprise Fund Proposal Document",
                 "Company Legal Name",
                 "CES ID Number",
                 "Sustaining Enterprise Fund",
                 "Nature of Business",
                 "DEVELOPMENT ADVISOR",
                 "DEPARTMENT MANAGER",
                 "Company Registration Number",
                 "Primary Bank",
                 "Contact Name",
                 "Base Employment"]

#Key info that we will add to all sheets
#This makes it easier for cross referencing in Excel Later
#we will attempt to add them to the table in the order listed - you probably want to list ID number first
ADD_INFO_TO_ALL_SHEETS = ["CES ID Number", "Company Legal Name"]

# Find and replace these tab names for the spreadsheet
#   Can have muliple variants (to allow to misspellings)
#   The match is on contains, letters and numbers only and ignores case
TAB_FIND_REPLACE={"YE":"Year End",
                  "YEamend":"Year End Amended",
                  "TrackRecord": "Track Record",
                  "DepartmentManagerName": "DM Comments",
                  "RESEARCHDEVELOPMENT": "R and D",
                  "EMPLOYMENT":"Employment",
                  "Cashflow":"Cash Flow",
                  "Cash Funding":"Cash Funding",
                  "Capital":"Capital",
                  "COMPANYDETAILS":"Company Details",
                  "ContactName":"Contact",
                  "IConfirmthatthecompany":"Declaration",
                  "ProjectCosts":"Project",
                  "Project":"Project",
                  "1StateBanks":"Support",
                  "DirectorName":"Director",
                  "ApplID":"Previous App",
                  "Tranche":"Repayment Calc",
                  "Key Info":"Key Info",
                  "SustainingEnterpriseFund":"SEF",
                  "Financedby":"Finance",
                  "Depreciation":"Depreciation",
                  "StatementOfComprehensiveIncome":"Income",
                  "StatementofFinancialPosition":"Balance Sheet",
                  "Impacts":"Impact",
                  "Checklist":"Checklist",
                  "StateBanks":"investors",
                  "StatementofComprehensiveIncom":"Income",
                  "CashInflows":"Cash",
                  "Creditors":"Creditors",
                  "Ihavereviewedtheproposal":"DM",
                  "WorkingCapital":"Working Capital",
                  "NeedForSupport":"Need",
                  "NetAssets":"Net Assets",
                  "Contact":"Contact",
                  "CapitalisationTable":"Capitalisation",
                  "ValueforMoney":"VFM",
                  "StateBanksGovernment":"External Support",
                  "KeyFinancials":"Key Financials",
                  "WorkingCapital":"Working Capital"

                  }

#Stop words to remove from text analysis
STOP_WORDS =[""]

