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


# 1 Next Sprint - complete merge
	* Merge in Dev (or discard)

	* Python client - from proxy.py ### next ##
		* use in all bot sampels
		* refactor project around this
		* config (from file - which url to check)

	* Separate client and server deploy
		perhaps a requirements clinet

	* finish langchain upgrade
		* get retriever chain and add
		* make current change use prompts
		* add vector retriever - use chain from this article https://python.langchain.com/docs/tutorials/retrievers/

	* Update Docs
		* migrate in docs
		* refer to example https://blog.langchain.dev/introducing-langserve/
		* refer to main source https://github.com/langchain-ai/langserve-launch-example?ref=blog.langchain.dev
		* add doc to key python files (especially app)

	* resetup 
		* docker (llama) image in docker?
		* (OR) instructions to run locally
		* docker build file open build kit


	* capture original examples and source
		* migrate in example https://blog.langchain.dev/introducing-langserve/
		* tmp project local - main source https://github.com/langchain-ai/langserve-launch-example?ref=blog.langchain.dev
		* Python client - from clienty.oy
		* refactor project around this
		* resup docker (llama)


	* merge in main (or discard)

# 1+ Sprint

* Poss outlook bot calling api

# 2nd Sprint
	* Test Bot working again
	* Unit testest bed
	* Try unit test in VSCode of main langchain class with different approaches
	* sanitze codebase (again) ahead of public release
	* Read and Tweak loading based on this langchain options -https://python.langchain.com/docs/modules/data_connection/document_transformers/
	* stoplist read from excel - valuable?
	* review python docs on bot, app, injest, rag_controller,
	* update promot
	* add topics
	* remove dear sir / signed bot
	* try again syndey / copilot

# 3rd sprint
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

* General Improvements
	* email templates
	* links in email templates
	* more filtering based on updated xl
	* categorisation of emails (to person best able to answer them, based on topics
	* loop and see if we can improve (langchain)
	* unit tests running

* Improvements - later NTH
	* named entities
	* Topic analysis
	* ?? Misfiled emails
	* ?? unanswered emails
	* POS tagging (counties but other keywords)
	* Postive or negative sentiment
	* get list of attached filenames
	* Emails without a response
	* Emails filed in the wrong folder
	* link email in chain (and recognize text)
	* suggest best email response (to draft?)
	* tag based on last person to answer client


# Improvements - later NTH
* named entities
* Topic analysis
* ?? Misfiled emails
* ?? unanswered emails
* POS tagging (counties but other keywords)
* Postive or negative sentiment
* LEO / County



## NEXT DO
* try out email generation - can I improve the prompt
* similar client search
* use / demo script and video
* tidy setup docs
* nth doc at module level for ingest and others


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
* XL streamlit
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
