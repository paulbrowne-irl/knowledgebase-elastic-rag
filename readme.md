# (Almost) Automatic responses to emails Emails using pre-collected Business Knowledge


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

## Work these into main body



## update day to day run instrauciotns
* project root # in main
* docker compose up # background infranstucure
* cd app
* uvicorn service.service_email:app (from app folder)
* check running at
* open windows client - streamlit run app.py (from app folder on windows)


Notes that need moved into the mainbd readme.md

* Edit / move Bot piece of docs to labs

* service API docs addd
    http://localhost:8000/docs
    include image screenshot-api.png


## Confidentiality of info

* Info stored locally
* LLM (Lllama) runs locally
* information redacted (see setting in config file is you wish to turn this off)
* Even with these precautions, probably better to injest *only* emails that ahve gone externally - since these have some exposure to the internet


## troubleshooting
Additional spacy:
* python -m spacy download en_core_web_sm
* python -m spacy download en_core_web_sm

#TODO - how to download

pytest - from root 
python -m pytest
run individula test - update pytest section

## Vscode Setup
Note on extra settings from settings.json



# OLDER BRANCH - POSSIBLE REMOVE to lab

* Note current snapshot of outlook plugin saved in GIST

## Outlook Extension - script lab

* Where to get from (link to Gist) - currently https://gist.github.com/paulbrowne-irl/dfe5e10bfe46182cf273217ae001b0de
* how to install scriptlab
* how to pin
* how to save (copy to clipboard - update Gitst)

## SSL Certs
* https://github.com/FiloSottile/mkcert
* https://dev.to/rajshirolkar/fastapi-over-https-for-development-on-windows-2p7d

## update start wtih ssl

OR uvicorn service.service_email:app 

## installing client only

* requirements-client.txt

## end Work these into main body

## Three main parts to the application: 
While they are linked, you will typically run only one at a time.
1. **Ingest** - load information (e.g. pdf or email) into the KnowledgeBase (Elastic)
1. **Bots** - Answer questions passed to it (to /from Excel) using RAG techniques. Designed to be used as part of Power Automate or other automatic workflow.
    * Sometimes these bots will depending on the REST server - but they will remind you to start it if needed
1. **App** - Friendly User Interface to answer questions in a back and forward way, focussing on 4 key business use cases.

## Underlying technologies:
* Choice of Large Language Model (LLM) - either local such as LLAMA or remote (e.g. Microsoft Copilot, OpenAI or Gemini).
* Elastic Search as the Vector search engine. Docker file gives "Human Friendly" UI (Kibana) for colleagues to fine-tune the retrieval search results.
* Langchain to integrate the above steps, but also allow for further extensions (choice of more LLMs, more document indexing, varying of steps in the response chain).
* Python scripts to implement
* (Optional) Streamlit for a user friendly UI 
* (Optional) Read / Writes files to Excel 365 - allows for integration with wider Office 365 and Power Automate workflows.
* (Optional) Outlook extension to auto-draft emails.

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
The scripts provide a simple service to expose a Rest API. To start the server (`service_email.py`)from the app folder:
    * `uvicorn service.service_email:app --reload`
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







