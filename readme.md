An AI Knowledgebase implementation using RAG (Retrieval Augmented Generation). Focuses on answering internal corporate queries (i.e. managing sensitive data, but also leveraging on a human-in-the-loop to both filter answers and provide feedback to learn) 


Underlying technologies are:
* Choice of Large Language Model (LLM) - either local or Microsoft Copilot.
* Elastic Search as the Vector search engine, but also "Human Friendly" UI for colleagues to fine-tune the retrieval search results.
* Langchain to integrate the above steps, but also allow for further extensions (choice of more LLMs, more document indexing, varying of steps in the response chain).
* Python scripts to implement
* (Optional) Streamlit for a user friendly UI 
* (Optional) Read / Writes files to Excel 365 - allows for integration with wider Office 365 and Power Automate workflows.


# Setup

Instructions for first time setup of the project:
    * Checkout / download this project as a folder onto the host computer

    * Docker - standard install (either Docker Desktop, or via WSL-Ubuntu)
        * You may also need to install the docker-compose plugin 

    * Python (3.12 or higher), install in the usual way.
        * Assuming Python pip and virtualenv tools are also installed

    * Install dependencies - in a terminal window, at the project root
        * Create environment: _virtualenv venv_
        * Activate environment: _source venv/bin/activate_
        * Install Python dependencies for this environment: _pip install -r requirements.txt_

    * Setup index in Elastic (first time only):
        * start Elastic (using docker compose up - see notes below):
        * open Kibana (see notes below)
        * setup indices - open this page http://localhost:5601/app/management/data/index_management/indices
            * test-can-del - used by unit tests
            * knowledge_base - the main index used to store documents

It is possible to install Elastic and Kibana directly on the machine (i.e. no Docker needed)


# Starting the background instructure

* Start the Docker Infrastructure 
    * Open terminal window, navigate to home folder containing docker-compose.yml
    * Start Elastic and Kibana using: _docker compose up_



# Running the application(s)

There are three main parts to the application; while they are linked, you will typically run only one 
1. Ingest ## update
1. Bot ## update
1. App - UI ## update

* Run the ingest scripts
    * Before using a Knowledgebase you obviously need to import knowledge into it. Each dataset is different, some sample scripts that you might wish to use as a starting point are in the **ingest.py** file. ### tidy
    * ### how to run in python ###
    * only need done once ##
    * probably need to clear beforehand

* Running the Bot
    * What is the bot ##
    * Update: (dependencies (e.g. sppreashdeet)
    * Why done this way?
        * simple data store
        * hosted in office 365


* Run the Web application
    * open the app folder: _cd app_
    * run Streamlit app to interact with documents local llm: _streamlit run app.py_

![Screenshot of Streamlit Web App](images/screenshot.jpg "Screenshot of Web App")




# Supporting Infrastructure

* Open the supporting documents  in a Web Browser
    *  The are several web pages to interact with the application. Assuming of course you have already ingested documents (see notes below)
    * Staring with most used page:
        * App available on http://localhost:8501 - screenshot below, this has several business use cases.
        * Kibana (Elastic Search Management tool) available on http://localhost:5601  - useful in managing the different "buckets" within the knowledgestore. ## admin and tweaking) ### this is useful for fine-tuning the search / similar documents being fed to the LLM.
        * Elastic Search available on  http://localhost:9200 - end point url, useful for verifying the retieval / search service is running
        * Portainer Web Management for Docker is available at https://localhost:9443 . This can safely be commented out in the docker-compose file but allows you to fine tune anything going wrong with the infrastructure.


* add images ####
    * running ES (screenshot from images folder link)
    * kibana (screenshot from images folder link)


# Running Unit Tests
* More info ###
    * running tests - go to app folder in terminal
        * single test: _python3 -m unittest tests.index_elastic_test_
        * all tests: _python3 -m unittest tests_

# Folders 
*  update #######

* templates ###
* new folders settings, data sample and output sample ####

* app - the main python web app
* app/pages - sub pages in the webapp
* app/ingest - python scripts to extract information and put it in the knowledgebase
* cache [local only] - local only backup of information
* images - for documentation
* data_no_share [local only] - some of the scripts may look to load information from here
* data-sample - sample pdf data (public source) to get started.


# Background reading and more information

The application draws on many concepts and articles - for example

* Original source notebook, RAG on Star Wars: 
    * https://colab.research.google.com/drive/11N01ssHqAXjW5NKJYkwT06V7RXLG4Yin#scrollTo=Sax1r_wW8kec
    * https://colab.research.google.com/github/elastic/blog-langchain-elasticsearch/blob/main/Notebooks/Privacy_first_AI_search_using_LangChain_and_Elasticsearch.ipynb?utm_source=pocket_saves

* Elastic search blog article : https://www.elastic.co/search-labs/blog/articles/privacy-first-ai-search-langchain-elasticsearch
* More info (On Langchain) https://python.langchain.com/docs/integrations/vectorstores/elasticsearch
