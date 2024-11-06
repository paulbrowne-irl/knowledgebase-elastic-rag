# AIM
* RAG that works standalone
* Works as business demo but allows deep dive    
* Can be pushed to public   
* Multiple, clear use cases using basic architecture   
* can link to excel or external helpdesk api

# 0 Alt streams

	* NEXT - end to end on static bot via rest API

	* update api to allow filter via local LLM - decide where
		* either own
		* first pass with clean prompt -https://github.com/takashiishida/cleanprompt

	* Outlook bot calling api via porxy
	 
	* Doc upgrade
		* check for todo
		* uvicorn service.simple_server:app to start service
		* remove older references (to labs)



# 1 Next Sprint - or move to later

	* NTH - Docker build for stability
		* try looking at python command (can set working direcotry?) - did that work
		* try copy into local cache folder
	
	* NTH - check if Index is there, create automatically if not in ingest.py
		* https://sarahleejane.github.io/learning/python/2015/10/14/creating-an-elastic-search-index-with-python.html
		* https://towardsdatascience.com/creating-and-managing-elasticsearch-indices-with-python-f676ff1c8113

	* NTH Ollama in docker file for ease of deployment
		* https://www.arsturn.com/blog/setting-up-ollama-with-docker-compose-a-complete-guide
		* anything useful (like devcontainers) to bring over?

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
	



# 2nd Sprint
	* Test Bot working again
	* Unit testable
	* Try unit test in VSCode of main langchain class with different approaches
	* review python docs on bot, app, ingest, rag_controller,
	* update promot
	
# 3rd sprint (triage)
	* move to unit testable 
	* try spidering web sources
	* Additional file format index: .txt and .xlsx and .pptx
	* Look at similar projects (send from firefox) - can we migrate to use that?
	* Consider filtering on sentences
	* try out microsoft phi instead of llama
	* similar client search
	* decide how to list topics
	* read info from key excel files (like questions or topics)
	* nth doc at module level for ingest and others
	* try out email generation - can I improve the prompt
	* Read and Tweak loading based on this langchain options -https://python.langchain.com/docs/modules/data_connection/document_transformers/

# relevant documents to read again
	* Ollama 
	
