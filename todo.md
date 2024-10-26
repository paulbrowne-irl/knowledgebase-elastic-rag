# AIM
* RAG that works standalone
* Works as business demo but allows deep dive    
* Can be pushed to public   
* Multiple, clear use cases using basic architecture   
* can link to excel or external helpdesk api

# 0 Alt streams

	* simple proxy.py running against server
	* try bot static - loop using proxy
	* update api to allow filter via local LLM - decide where	
	* Poss outlook bot calling api
	* Doc upgrade
	* simple email bot using proxy


# 1 Next Sprint - or move to later

	* NTH - Docker build for stability
		* try looking at python command (can set working direcotry?) - did that work
		* try copy into local cache folder

	* Ollama in docker file for ease of deployment
		* https://www.arsturn.com/blog/setting-up-ollama-with-docker-compose-a-complete-guide
		* anything useful (like devcontainers) to bring over?

	* true langserve code
	* read langserve book
	* restore sydney or other copilot

	* refer to example https://blog.langchain.dev/introducing-langserve/
	* refer to main source https://github.com/langchain-ai/langserve-launch-example?ref=blog.langchain.dev
	* add doc to key python files (especially app)
	



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


	