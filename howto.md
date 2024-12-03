# HOW TO do Common project tasks

This are tasks commonly carried out by Dev and Project Admin. 


## New Release

* run automatic tests
* manual tests - see anything
* pip freeze requirements.txt
* Update Docker file
* Tag on Github
* Create Stable Branch
* Bugfixes

## Docker Build

How to create a new docker build

* run build  ## notes in docker file
* Update these notes ## TODO


# Development notes

## Key folders  
* High level folders

* Main application is in the `app` folder:    
    * `app/cache` [local only] - local only backup of information
    * `app/service` - server and backed creating llm chains and executing them
    * `app/settings` - configuration files
    * `app/pages` - sub pages in the webapp
    * `app/templates` template files for prompts (to AI) and emails responses
    * `app/util` - supporting scripts to implement data extraction, indexing to elastic, language process, reading-writing office files, implemeting RAG. More notes on these in the sub folders.
* Other folders in the project:
    * `tests` - unit tests for the application
    * `data-sample` - sample public documents to get you started with the scripts (e.g. Ingest then ask questions against)
    * `data_share` [local only] - some of the scripts may look to load information from here e.g. 

## Running Unit Tests
To run the Unit tests
* Open the app folder: `cd app` in a terminal window
* Activate the Python environment with dependencies you installed earelier: `source venv/bin/activate`
* Choose which type of test you want to run
        * single test: `python3 -m unittest tests.index_elastic_test`
        * all tests: `python3 -m unittest tests`


## Background reading and more information

The application draws on many concepts and articles - for example
* Original source notebook, RAG on Star Wars: 
    * https://colab.research.google.com/drive/11N01ssHqAXjW5NKJYkwT06V7RXLG4Yin#scrollTo=Sax1r_wW8kec
    * https://colab.research.google.com/github/elastic/blog-langchain-elasticsearch/blob/main/Notebooks/Privacy_first_AI_search_using_LangChain_and_Elasticsearch.ipynb

Background information and links when developing this project
* Elastic search blog article : https://www.elastic.co/search-labs/blog/articles/privacy-first-ai-search-langchain-elasticsearch
* More info (On Langchain) https://python.langchain.com/docs/integrations/vectorstores/elasticsearch
* https://www.elastic.co/blog/getting-started-with-the-elastic-stack-and-docker-compose (Part 1 of 2)
* Setup Elasticsearch UI -https://docs.elastic.co/search-ui/tutorials/elasticsearch
* Kibana API requests - https://www.elastic.co/guide/en/kibana/current/console-kibana.html
* Elastic Search Getting started - https://www.elastic.co/guide/en/workplace-search/8.7/workplace-search-getting-started.html
* Search UI with elastic search - 	• https://docs.elastic.co/search-ui/tutorials/elasticsearch

More information on Open Web UI and Ollama
* https://www.arsturn.com/blog/setting-up-ollama-with-docker-compose-a-complete-guide
* https://hub.docker.com/r/ollama/ollama
* https://medium.com/@edu.ukulelekim/how-to-locally-deploy-ollama-and-open-webui-with-docker-compose-318f0582e01f

## Corporate deploy

How to deploy in a corporate environment i.e. specific settings that you don't want to share back to GitHub, while still being able to access teh latest code

### files to copy
* config-overwrite.conf

### files to review
* settings in config.conf
* review todo.md - any dev changes needing reverting
* any tokens needed in token-storage-local.json

### Other todo
* consider delete and recreate virtualenv   
* consider updating requirements snapshot pip freeze > snapshot-requirements.txt




