# AIM

* RAG that works standalone
* Works as business demo but allows deep dive
* Can be pushed to public
* Multiple, clear use cases using basic architecture
* can link to excel or external helpdesk api

## 0 Next sprint - simple working day-to-day bot for video and base for iteration

* NEXT - Link LLM


  * First pass at release
    * Mark and integrate ???
	* read and edit
	* tidy of howto.md
	* tidy of todo.md
	  * another read through
	  * update outlook section with screenshots
	* Pull in video
  
  * Wire in call to LLM
    * Python services
    * -- spin up infrastructure (Docker compose)
    * -- spin up unicorn (Python on Bash)

    * NEXT: Test run Windows / Outlook client
      * try rest client test 
        * try move to POST format
      * New Class to parse format
        * Unit test
        * copy existing format  
        * url decode
      
      * test each different llm
        * see if can get format back - hardcode to pickle
        * use pickle to test if can handle
        * remove test code

  * Basic Outlook tuning - sort
  * fix Reply all (possible to set from?)
    * run on multinbox (NTH)
    * exclude mails from [list]
    * always cc [list]

  * Update OpenAI to Azure
   	* investigate account
   	* add to config

  * Make streamlit page screenshot friendly
    * check other UI Elements
    * remove other pages (?) or inital tidy
    * video demo

  * PyTest
    * updrade simple one in python - as test client (or just note test in howto?)
    * PyTest on Uvicorn - <https://stackoverflow.com/questions/57412825/how-to-start-a-uvicorn-fastapi-in-background-when-testing-with-pytest/57829525>
    * Google way of pytest stream lit
    * Stub out pyTest on Helper (??)
    * stub out more pytests on streamlit
    * stub out more pytests on helper

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

* Milestone - "good enough" version for right now
  * Push to main
  * Focus on last improvements before 'release'
  * tag release candidate
  * branch
  * setup 'main' vscode project ready to use day-to-day

## 1 Hold back from current push as not strictly needed

* NTH ---------------------------
  * script to bring up all servers (streamlist and api)
  * update to doc

* loop and show the values being pulled back
  * fine tune results
  * fine tune prompt
  * fine tune llm
  * check redeaction / restore and what local service is storing in "db"

* try build as listed in dockerfile
  * push to docker hub
  * list in docker compose for "stable release"

* Streamlit
  * make notes of refactor into true standalone client
  * API "ask a DA question" on other pages

* UI
  * Email categories that will be marked as processed

## 2 Next Sprint - or move to later

* Automate tests in Github - <https://docs.streamlit.io/develop/concepts/app-testing/automate-tests>

* refactor remove chain factory
* API - create one server with all services
* tidy vscode - make available as devcontainer

* NTH - check if Index is there, create automatically if not in ingest.py
* <https://sarahleejane.github.io/learning/python/2015/10/14/creating-an-elastic-search-index-with-python.html>
* <https://towardsdatascience.com/creating-and-managing-elasticsearch-indices-with-python-f676ff1c8113>

* true langserve code
* Read Background <https://www.datacamp.com/tutorial/deploying-llm-applications-with-langserve>
* Read  Blog post - <https://blog.langchain.dev/introducing-langserve/>

* extract key terms from document (based on MTU)
* <https://python.langchain.com/docs/tutorials/classification/>

* read langserve book
* restore sydney or other copilot

* refer to example <https://blog.langchain.dev/introducing-langserve/>
* refer to main source <https://github.com/langchain-ai/langserve-launch-example?ref=blog.langchain.dev>
* add doc to key python files (especially app)

* refactor other bots / app to use client-server example (if needed)

## Backlog

* review python docs on bot, app, ingest, rag_controller,
* Later - more tests and other project best practice from <https://pytest-cookbook.com/>
* try spidering web sources
* Additional file format index: .txt and .xlsx and .pptx
* Look at similar projects (send from firefox) - can we migrate to use that?
* similar client search
* decide how to list topics
* read info from key excel files (like questions or topics)
* nth doc at module level for ingest and others

## Backlog - Langchain and LLMs

* Try unit test in VSCode of main langchain class with different approaches
* update prompts - improve email generation
* try out microsoft phi instead of llama [search for docker image]
* Read and Tweak loading based on this langchain options -<https://python.langchain.com/docs/modules/data_connection/document_transformers/>

## Future Features

* setup code so that it can be called from Power Automate
* Chain local and remote LLMs
