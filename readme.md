An AI Knowledgebase implementation using RAG (Retrieval Augmented Generation). Underlying technologies are choice of LLM (either local or Copilot), Elastic for Vector search, with a Streamlit UI. Also provides Notebooks and other Python Scripts to ingest data into the Knowledgebase.

# Setup

* Instructions 
    * Checkout / download this project as a folder onto the host computer
    * Docker - standard install (either Docker Desktop, or via WSL-Ubunto)
    * Python (3.10 or higher) install in the usual way.
    * Install dependencies - in a terminal window
        * Create environment _virtualenv venv_
        * Activate environment _source venv/bin/activate_
        * Install Python dependencies for this environment using the list provided _pip install -r requirements.txt_

# Integrate notes
* running bot.py
* templates


# Running the application

* Start the Docker Infrastructure 
    * Open terminal window, navigate to home folder containing docker-compose.yml
    * Start Elastic and Kibana using _docker-compose up_

* Run the Web application
    * open the app folder _cd app_
    * run Streamlit app to interact with documents local llm _streamlit run app.py_

* Open the application in a Web Browser
    *  The are several web pages to interact with the application. Assuming of course you have already ingested documents (see notes below)
    * Staring with most used page:
        * App available on http://localhost:8501 - screenshot below, this has several business use cases.
        * Elastic Search available on  http://localhost:9200 - this is useful for fine-tuning the search / similar documents being fed to the LLM.
        * Kibana available on http://localhost:5601  - useful in managing the different "buckets" within the knowledgestore.
        * Portainer Web Management for Docker is avaailable at https://localhost:9443 . This can safely be commented out in the docker-compose file but allows you to fine tune anything going wrong with the infrastructure.

![Screenshow of Streamlit Web App](images/screenshot.jpg "Screenshot of Web App")

# Ingesting documents

Before using a Knowledgebase you obviously need to import knowledge into it. Each dataset is different, some sample scripts that you might wish to use as a starting point are in the **app/ingest** folder.

# Folders
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
