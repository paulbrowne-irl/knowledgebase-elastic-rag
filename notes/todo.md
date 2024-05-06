# AIM

* RAG that works standalone
* Works as business demo
* allows deep dive 
* Can be pushed to public
* Multiple, clear use cases using basic architecture


# AIM BOT

* see todo-bot.md



# AIM NEXT ITERATION

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


## NEEDED DOCS

* note what expected setup elastic
* note what exepect import financials
* note how to run ingest pdf, ingest emails
 Tidy setup notes (if external needed)

## NEEDED EMAILS

* update settings for app
* Import to elastic
* try search
* update example against new index
* (EAR) tweak to get as many emails xtracted as possible


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
* ingest - replace from langchain_elasticsearch import ElasticsearchStore
	* #from langchain_community.vectorstores.elasticsearch import 
	* from langchain_elasticsearch import ApproxRetrievalStrategy
* pull in logging
* Resolve langchain warning messages
* resolve Pandas warning message
* Resolve token indices lentgth warning (shorter index)
* Resolve warning - ElasticVectorSearch will be removed in a future release


# IDEAS FUTURE ITERATION
* XL streamlit
* elastic 
* XL indeox - using Eland (find article - C:\Users\pbrowne\projects\local analysis data)
* sample charts?
* embed xl 
* pull in SMART keywords to index
* how to implmenet filter of data https://python.langchain.com/docs/integrations/vectorstores/elasticsearch



# TIDY LABS INTO INTO MAIN
* add/index emails (outlook) - SAMPLE - answer an email
* add/index financial SEF data - SAMPLE - extract infroamtion
* add/index sample using grant payments - SAMPLE - answer information on processing
* add/index SEF text data - SAMPLE -scheme review
* add/index "companies like this" - SAMPLE - recruitment


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
