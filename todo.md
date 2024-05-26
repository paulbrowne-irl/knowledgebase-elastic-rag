# AIM

* RAG that works standalone
* Works as business demo
* allows deep dive 
* Can be pushed to public
* Multiple, clear use cases using basic architecture

# Next sprint
1. multi dir read

	* restore code line 118

1. first pass read queestions from sample file
1. loop and call llm
	* restore code
1. update back to excel (fwith flag?)
1. random time in loop
1. add (more) python types / safety (like on injest)


# 2nd sprint
1. config two sources on silver

# 3rd sprint
* 3 documents back	
* ensure we have a link back to source doc
* move to unit testable 
* find except , add logging.exception() to it
* sanitze codebase ahead of public push



# Add to doc
* Llama3 setup - pull from lab



# Tidy these into main list
* stoplist read from excel
* Atext injest, FAQ document
* Look at similar projects (send from firefox) - can we migrate to use that?




# NEXT - UPGRADE BOT SEARCHING AGAINST INDEX

* run and review indexed data - 	








# Later - Iterate
* update promot
	* add topics
	* remove dear sir / signed bot
* [later] map topics to emails / areas of interest
	* decide how to list topics
	* read info from key excel files (like questions or topics)
* Other Info
	* any other meta data on docs
	* any other doc types to ingst

* Get unit tests working agiain

* Consider filtering on sentences

* Index other documents
	* powerpoint

* Read and Tweak loading based on this langchain options -https://python.langchain.com/docs/modules/data_connection/document_transformers/

* Final Decide folderstruture
	* some sort of .ini file
		* keywords / topics
		* name of owner ?? or keep that in 

# SENTIMENT ADD
	
	* Add from calc_sentiment.py
		* get topics from emails using injest method
		* sentiment etc f



# Improvements - later priority
* Prompts
* email templates
* links in email templates
* langchain
* more filtering based on updated xl
* categorisation of emails (to person best able to answer them, based on topics
* loop and see if we can improve (langchain)
* unit tests running


# Improvements - later NTH
* Llama 3
* named entities
* Topic analysis
* ?? Misfiled emails
* ?? unanswered emails
* POS tagging (counties but other keywords)
* Postive or negative sentiment
* LEO / County


## next Problems I want to solve
* get list of attached filenames
* Emails without a response
* Emails filed in the wrong folder
* link email in chain (and recognize text)
* suggest best email response (to draft?)
* tag based on last person to answer client

* identify most relevant colleauges
* Save attachments / call rules?
* identify topics / keywords



# AIM NEXT ITERATION+1

** Helpdesk using internal detailled info (like emails)
** Detailled financial analysis - 
** Sanitized public / internal sharable version


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
* pull in better docs (from external index)
* Silver: tweaks to streamlit to accomodate Q&A *on_text* for the moment
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
