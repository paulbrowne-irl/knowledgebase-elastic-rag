A RAG implementation using Elastic and LLM, with a Streamlit UI. Notebook to ingest data.

# Setup

* Requirements - Docker, Python (3.10)
* Create environment _virtualenv venv_
* Activate env _source venv/bin/activate_
* Install dependencies _pip install -r requirements.txt_
* Start Elastic and Kibana _using docker-compose up_
* Portainer Web Management for Docker is avaailable at https://localhost:9443 . This can safely be commented out in the docker-compose file

# Running (in app folder)
* open the app folder _cd app_
* run Streamlit app to interact with documents local llm _streamlit run poc.py_
* App available on http://localhost:8501 , elastic available on  http://localhost:9200, Kibana available on http://localhost:5601 


# Ingesting documents

* TODO more info on Ingest documents using notebook 

# otherstarting points
* add

# Folders
* app
* ingest
* merge
* lab
* data 
* data-sample




# Notes and original sources

* From notebook: https://colab.research.google.com/drive/11N01ssHqAXjW5NKJYkwT06V7RXLG4Yin#scrollTo=Sax1r_wW8kec

* Original https://colab.research.google.com/github/elastic/blog-langchain-elasticsearch/blob/main/Notebooks/Privacy_first_AI_search_using_LangChain_and_Elasticsearch.ipynb?utm_source=pocket_saves

* From elastic search blog article : https://www.elastic.co/search-labs/blog/articles/privacy-first-ai-search-langchain-elasticsearch

* More info (from Langchain) https://python.langchain.com/docs/integrations/vectorstores/elasticsearch
