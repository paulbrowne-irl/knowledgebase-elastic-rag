# Respond to Emails using Local Knowledge


Many organisations/individuals have piles of documents containing valuable information but are little used after their initial creation.

"RAG" techniques allow you and colleagues to chat with these documents - allowing you to combine the accuracy of the documents and the "chattiness" of AIs like ChatGPT. More backgound to RAG in the links at the end of this page.

This project is code to implement a pilot RAG Chatbot in a not for profit VC. Given the community nature of the organisation (and the out-of-hours development) it is shared for reuse. It focuses on answering internal corporate queries (i.e. managing sensitive data, but also leveraging on a human-in-the-loop to both filter answers and provide feedback to learn) 

For obvious reasons only generic code and no information / knowledge is shared - this has the benefit of you being able to add your own documents. See instructions below.

<img src="images/screenshot.jpg" width="30%" height="30%" />

## Key sections in this guide
* [Setup](#Setup)
* [Starting the background infrastructure](#Starting-the-background-infrastructure)
* [Running the Ingest Script](#Running-the-Ingest-Script)
* [Config](#Config)
* [Running the Application and Bot](#Running-the-Application-and-Bot)
* [Key folders](#Key-folders)

## Three main parts to the application: 
While they are linked, you will typically run only one at a time.
1. **Ingest** - load information (e.g. pdf or email) into the KnowledgeBase (Elastic)
1. **Bots** - Answer questions passed to it (to /from Excel) using RAG techniques. Designed to be used as part of Power Automate or other automatic workflow.
    * Sometimes these bots will depending on the REST server - but they will remind you to start it if needed
1. **App** - Friendly User Interface to answer questions in a back and forward way, focussing on 4 key business use cases.

## Underlying technologies:
* Choice of Large Language Model (LLM) - either local or Microsoft Copilot.
* Elastic Search as the Vector search engine, but also "Human Friendly" UI for colleagues to fine-tune the retrieval search results.
* Langchain to integrate the above steps, but also allow for further extensions (choice of more LLMs, more document indexing, varying of steps in the response chain).
* Python scripts to implement
* (Optional) Streamlit for a user friendly UI 
* (Optional) Read / Writes files to Excel 365 - allows for integration with wider Office 365 and Power Automate workflows.


## First time Setup

Instructions for first time setup of the project:
1. Checkout / download this project as a folder onto the host computer

1. Install Docker - standard install (either Docker Desktop, or via WSL-Ubuntu).You may also need to install the docker-compose plugin
    * https://docs.docker.com/engine/install/ubuntu/
    * For most systems this is `sudo apt install docker.io` and docker compose `sudo apt-get install docker-compose-plugin`

1. Install Python (3.12 or higher) in the usual way. Python `pip` and `virtualenv` tools are also needed.
    * check first what version you have installed using `python -V`

1. Install Python dependencies - in a terminal window, at the project root
    * Create virtual environment: `virtualenv venv`
    * Activate virtual environment: `source venv/bin/activate`
    * Install Python dependencies for this environment: `pip install -r requirements.txt`

1. Using a Local LLM - first time setup
    * The config file gives the option of passing questions a *private* local LLM using Ollama (e.g. Llama 3.2 from Meta). The Docker file can help you run this local LLM.
        * Check the `docker-compose.yml` file so that the "Ollama" and "OpenWebUI" are not commented out.
        * OpenWebUI is optional , but provides a useful web interface on http://localhost:3000
    * Start Docker as normal using `docker compose up`		
    * Ollama provides the infastructure - you will need to tell it (first time) which LLM to use.
        * Open a new console / terminal
        * Pull the relevant llm `docker exec -it ollama ollama run llama3.2`

1. Setup index in Elastic (first time only):
    * Start Elastic (using `docker compose up` from the root folder of the project.
    * Open Kibana (see notes below)
    * Setup indices - open this page  http://localhost:5601/app/management/data/index_management/indices
        * `test-can-del` - used by unit tests
        * `knowledge_base` - the main index used to store documents
    * Useful commands (in the dev console window of Kibana)
        * Delete an index  `DELETE /knowledge_base`
        * Create an index `PUT /knowledge_base`


It is possible to install Elastic and Kibana directly on the machine (i.e. no Docker needed), please refer to the Elastic / Kibana home page for instructions - https://www.elastic.co/

## Configuration
* The main confirmation file is  in `app/config/config.conf` 
    * Please edit this or see the notes in the `app/config` folder to customize configuration. 
    * This config file is shared for the ingest script, the Bot and the Application.
* Some APIs (Copilot, OpenAI, Teamworks helpdesk) require tokens the first time the are run. Please consult the documentation to retrieve these. The script will ask you for these and store locally. This is a plain text json file(`token-storage-local.json`). While it is excluded from git, you may wish to review how has access to it.

# Running the application

## Starting the background infrastructure

A Docker compose file is provided to make it easy to download and run the supporting infrastructure (e.g. the Elastic Search engine). To start this Infrastructure using Docker:
* Open a (new) terminal window, navigate to home folder containing docker-compose.yml
* Start Elastic and Kibana and other services using: `docker compose up`

You can check if the Elastic Search Service is running using the url http://localhost:9200/. You should see a success message similar to the screenshot below.

![Screenshot of ElasticSearch API - use to check if service is working](images/es-screenshot-port-9200.png "Screenshot of ElasticSearch API - use to check if service is working")

The Kibana App runs on top of Elastic and allows you to create indexs to store and search data. It is also useful in fine-tuning the searches so that we can pass more relevant documents as a prompt to the large language model. Kibana (Elastic Search Management tool) available on http://localhost:5601

![Screenshot of Kibana Tools - used to create, manage, tune searches in the Knowledgebase](images/kibana`index`management.png "Screenshot of Kibana Tools - used to create, manage, tune searches in the Knowledgebase") 

No screenshot, but also automatically started is the Portainer Web Management for Docker, available at https://localhost:9443 . This can safely be commented out in the docker-compose file if this is not needed.


## Running the Application and Bot

The application is a UI, easier to use. The Bot is semi-automatic and does many of the same things, but as part of a process flow

### Running the Service 
The scripts provide a simple service to expose a Rest API. To start the server (`simple_server.py`)from the app folder:
    * `uvicorn service.simple_server:app --reload`
    * Open a web browser to view the REST api on http://localhost:8001/docs

Note that some other examples (some bots) depend on this server - but should remind you to start it if needed.

### Running the Ingest Script 

Before using a Knowledgebase you obviously need to import knowledge into it. 
* The main script to ingest data is in the `app/ingest.py` . 
* This script will take a starting folder and index most of the files (pdf, messages , word docs) found in that folder. It will also find sub-folders and index those recursivly.

To run the ingest script
* Open the app folder: `cd app` in a terminal window
* Activate the Python environment with dependencies you installed earelier: `source venv/bin/activate`
* Run the script using `python ingest.py`
    * (You may need to be more version specific e.g. python3 ingest.py)

In general, you will only need the ingest script once (or infrequently, if you wise to add more documents). For small datasets, it is probably easier to delete the Knowledgebase index (using Kibana - see link and screenshot above), then run the Ingest script again.


### Running the Bot - Excel

Typical flow for the Bot is to read a question from Excel, apply RAG techniques to answer the question, then save the answer back in Excel. Since the Excel file can be hosted online, this allows Integration with Office 365 and Power Automate. e.g.
1. The User can ask a question on Microsoft Forms
1. Power Automate saves this question in Excel.
1. The Bot reads the question, saves the answer back in Excel.
1. Human can review the answer, update the line in Excel if they are happy with it.
1. Power Automate can send back the answer to the original person using email.

To run the bot.
* Open the app folder: `cd app` in a terminal window
* Activate the Python environment with dependencies you installed earelier: `source venv/bin/activate`
* Run the script using `python bot_excel.py`

### Running the Web Application
The Web application addresses a wider range of business use cases than the bot - see the tabs on the left hand side of the screenshot below.

To run the Web Application.
* Open the app folder: `cd app` in a terminal window
* Activate the Python environment with dependencies you installed earelier: `source venv/bin/activate`
* Run Streamlit app to interact with documents local llm: `streamlit run app.py`
* App available on http://localhost:8501 

![Screenshot of Streamlit Web App](images/screenshot.jpg "Screenshot of Web App")



# Development notes

## Key folders  
* High level folders
    * `data-sample` - sample public documents to get you started with the scripts (e.g. Ingest then ask questions against)
* Main application is in the `app` folder    
    * `app/cache` [local only] - local only backup of information
    * `data_share` [local only] - some of the scripts may look to load information from here
    * `app/langserve` - server and backed creating llm chains and executing them
    * `app/pages` - sub pages in the webapp
    * `app/settings` - configuration files
    * `app/templates` template files for prompts and emails
    * `app/tests` - unit tests for the application
    * `app/util` - supporting scripts to implement data extraction, indexing to elastic, language process, reading-writing office files, implemeting RAG. More notes on these in the sub folders.


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







