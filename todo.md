# AIM
* RAG that works standalone
* Works as business demo but allows deep dive    
* Can be pushed to public   
* Multiple, clear use cases using basic architecture   
* can link to excel or external helpdesk api


# NEXT
* stub bot api using code
	* refactor api call code
* update llm models   
* try latest docs and test 
	- load latest data
	- chje
* what other data formats to load
* config to openai
* drop / reindex single folder or document


* run bot and test
	* "Good enough" solution for answering questions (lllama or other)
	* test can pull back sources and other meta into results - bot   

* run all unit tess see if can resolve   

# 2nd Sprint
* Test Bot working again
* test meta data coming through to Bot XL



# 3rd sprint
* Unit testest bed
Try unit test in VSCode of main langchain class with different approaches
* sanitze codebase (again) ahead of public release
* Read and Tweak loading based on this langchain options -https://python.langchain.com/docs/modules/data_connection/document_transformers/
* stoplist read from excel - valuable?
* review python docs on bot, app, injest, rag_controller,
* update promot
	* add topics
	* remove dear sir / signed bot
* try again syndey / copilot

# 4th sprint
* 3 documents back and use langchain llm to summarize
* move to unit testable 
* try spidering web sources
* eland query summarise kb or other export
* Additional file format index: .txt and .xlsx and .pptx
* Look at similar projects (send from firefox) - can we migrate to use that?
* Consider filtering on sentences



# Later - Iterate
* try out microsoft phi instead of llama
* [later] map topics to emails / areas of interest
	* decide how to list topics
	* read info from key excel files (like questions or topics)
* [later] sentiment add
	
	* Add from calc_sentiment.py
		* get topics from emails using injest method
		* sentiment etc f



# Improvements - later priority
* email templates
* links in email templates
* more filtering based on updated xl
* categorisation of emails (to person best able to answer them, based on topics
* loop and see if we can improve (langchain)
* unit tests running


# Improvements - later NTH
* named entities
* Topic analysis
* ?? Misfiled emails
* ?? unanswered emails
* POS tagging (counties but other keywords)
* Postive or negative sentiment
* LEO / County



## NEXT DO
* test and debug all screens
	* more more robust grsphs
	* try out email generation - can I improve the prompt
	* similar client search
	* Local LLM see if can restore LLMChain (or similar)
* read langchain docs
* purge any email data, code data : delete history on git
* check what email data we have / can we updated the prompt


* use / demo script and video
* tidy setup docs
* nth doc at module level for ingest and others



 Tidy setup notes (if external needed)


## NEEDED DATA
* Power BI Datagrab
* Reindex main docs
* Index Excel data (wdier)
* SEF Data:  By Sector / Mediam / Normal discribution / company as outlier
* run email extract again
* convert xls to elastic


# HOLD SAMPLE - FOR FUTURE INTERATIONS 
* DA QA - test with questions
* Setup Alert - create but blanck
* Similar companies - list out, 
	* OK for now
* Financials - bring through sample	
* Email - update prompt
	* Better prompt for generating email
	* some sort of graph of key terms



# NEXT 
* see what documents are indexed
* UI tweaks to streamlit to accomodate Q&A *on_text* for the moment
* displaydocs better in similarity search
* update home page (with RAG model)
* stub out look and feel of other apps
* better updates on QA



# NEEDED - HOUSEKEEPING

* resolve Pandas warning message
* Resolve token indices lentgth warning (shorter index)



# IDEAS FUTURE ITERATION
* XL streamlit
* elastic 
* XL indeox - using Eland (find article - C:\Users\pbrowne\projects\local analysis data)
* sample charts?
* embed xl 
* pull in SMART keywords to index
* how to implmenet filter of data https://python.langchain.com/docs/integrations/vectorstores/elasticsearch




# ITERATE
* Better Search (by Keywords)
* NER on incoming datat
* Better LLM models
* better table info
* being load of more relevant info (find)
* bring in NER and other processing from other project
* Add Public / Private Switch





# EXPLORE LOOK AT
* Eland - for datascience 
* NLP via eland https://www.elastic.co/guide/en/machine-learning/current/ml-nlp-ner-example.html
* Langchain sample
* Milo for data



# EXPLORE POSSIBLE NEXT STEPS
	• POC basics
		○ Prompt engineering - can co-pilot summarize manunally
			§ Reduce down
		○ Cross check
			§ What RSM want - can I Index by keywords / synonums?
	
	• Articles (to shortcut)
		○ Indexing in elastic
		○ Ffinding and feeding into REAG
	• Code - review existing
		○ PDF extraction
		○ Word extraction etc 
	• Notes to self
		○ Reason for using elastic - able to view data before retrieval	
Can setup simple search, then elaborate using previous text technqiutes
