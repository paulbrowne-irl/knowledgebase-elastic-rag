# AIM
* RAG that works standalone
* Works as business demo but allows deep dive    
* Can be pushed to public   
* Multiple, clear use cases using basic architecture   
* can link to excel or external helpdesk api

# 0 Next sprint - simple working day-to-day bot for video and base for iteration


	* Email bot 
		* Stub outline based on tmp-Outlook
			* bring in
			* delete folder
		* setup streamlit page with loop
			* tidy existing
			* new page
			* setup PyTest
				* Google way of pytest stream lit
			* setup loop on page
				* Read Config and present on page
					* starting folder (email box / sub folder)
					* reply as?
					* start and end portion of text to send to LLM
					* Go button
				* start in config (folders) - for each email
					* get text from email
					* do call to llm using text
					* mark as "done" using category
					* reply 
					* do call using text
					* add text to email
				* Streamlit logging on screen (to show activity)
				* Make strealit page screenshot friendly
				


		* outlook add in wiht streamlit page
			* Break out instrucionts in tmp-appendix2.docx -> Readme-add (will need new screenshot)



		* updrade simple one in python - as test client (or just note test in howto?)
			* PyTest on Uvicorn - https://stackoverflow.com/questions/57412825/how-to-start-a-uvicorn-fastapi-in-background-when-testing-with-pytest/57829525

		* Streamlit
			* make sure streamlit app is working
			* make notes of refactor into try standalong client
				* API "ask a DA question" etc
			* Stub streamlit "read emails" page
				* run on start up?
				* read config
				* logging to screen?



	* Doc upgrade
		* move folder notes in howto.md into __init__ in each / readme.txt
		* anything in in readme-add
		* tidy overall strcuture
		* screenshot screenlit and make note of use cases
		* screenshot new api 
		* remove older references (to labs)
		* Outlook plugin?
			* screenshot
		* what in Doc can I move to HOWTO.md
			* tidy howto.md

	* Clear Elastic, run ingest with latest dataset
		* tune on chunks generates

	* loop and show the values being pulled back
		* fine tune results
		* fine tune prompt
		* fine tune llm
		* check redeaction / restore and what local service is storing in "db"



	* try build as listed in dockerfile
		* push to docker hub
		* list in docker compose for "stable release"
	
	* Push to main, release
		* tag dev candidate
		* 

	* NTH
		* script to bring up all servers (streamlist and api)
			* update to doc
		


# 1 Next Sprint - or move to later

	* refactor remove chain factory
	* API - create one server with all services
	* tidy vscode - make available as devcontainer

	
	* NTH - check if Index is there, create automatically if not in ingest.py
		* https://sarahleejane.github.io/learning/python/2015/10/14/creating-an-elastic-search-index-with-python.html
		* https://towardsdatascience.com/creating-and-managing-elasticsearch-indices-with-python-f676ff1c8113

	* true langserve code
		* Read Background https://www.datacamp.com/tutorial/deploying-llm-applications-with-langserve
		* Read 	Blog post - https://blog.langchain.dev/introducing-langserve/

	* extract key terms from document (based on MTU)
		* https://python.langchain.com/docs/tutorials/classification/

	* read langserve book
	* restore sydney or other copilot

	* refer to example https://blog.langchain.dev/introducing-langserve/
	* refer to main source https://github.com/langchain-ai/langserve-launch-example?ref=blog.langchain.dev
	* add doc to key python files (especially app)

	* refactor other bots / app to use client-server example (if needed)
	



# Backlog 

	* review python docs on bot, app, ingest, rag_controller,
	* Later - more tests and other project best practice from https://pytest-cookbook.com/
	* try spidering web sources
	* Additional file format index: .txt and .xlsx and .pptx
	* Look at similar projects (send from firefox) - can we migrate to use that?
	* similar client search
	* decide how to list topics
	* read info from key excel files (like questions or topics)
	* nth doc at module level for ingest and others



# Backlog - Langchain and LLMs
	* Try unit test in VSCode of main langchain class with different approaches
	* update prompts - improve email generation
	* try out microsoft phi instead of llama [search for docker image]	
	* Read and Tweak loading based on this langchain options -https://python.langchain.com/docs/modules/data_connection/document_transformers/
	

# Future Features
	* setup code so that it can be called from Power Automate
	* Chain local and remote LLMs
