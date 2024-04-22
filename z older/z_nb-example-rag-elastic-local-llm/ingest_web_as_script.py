# Imports
# Make sure the requirements are installed using pip install -r requirements.txt

import re
import requests
from bs4 import BeautifulSoup
import pickle
import json
from tqdm import tqdm
from langchain.embeddings import HuggingFaceEmbeddings

from getpass import getpass
from pathlib import Path
from langchain.vectorstores import ElasticVectorSearch
from pathlib import Path

#########
# passwords for elastic
# endpoint = "3dd138be8cc44d2fa2bc0bb58720ab8a.us-central1.gcp.cloud.es.io"
# username = "elastic"
# password = "KDGbcC0FKi290qz18EbTKGBB"

endpoint = "localhost"
#username = "elastic"
#password = "9+KjRVIwctnHhsgCQs_y"


#es_url =  f"https://{username}:{password}@{endpoint}:9200"
es_url =  f"http://{endpoint}:9200"

print ("Using URL "+es_url)


# # Scraping a small set of data from Wookieepedia
# 
# We'll keep it to two pages for characters active in recent TV shows, too recent for updates to be caught by common 2021 AI data sets.
# 
# Check out the original article and origin of this parsing exmaple over at: https://towardsdatascience.com/star-wars-data-science-d32acde3432d

#

#
scraped = {}
pages = [
    "https://starwars.fandom.com/wiki/N-1_starfighter",
    "https://starwars.fandom.com/wiki/Ahsoka_Tano",
    "https://starwars.fandom.com/wiki/Din_Djarin"]

last_number = 0
for page_url in pages:
    try:

        # Get page
        result = requests.get(page_url)
        content = result.content
        soup = BeautifulSoup(content, "html.parser")

        # Get title
        heading = soup.find('h1', id='firstHeading')
        if heading is None: continue
        heading = heading.text

        # Extract Sidebar
        is_character = False
        side_bar = {}
        sec = soup.find_all('section', class_='pi-item')
        for s in sec:
            title = s.find('h2')
            if title is None:
                title = '<no category>'
            else:
                title = title.text
            side_bar[title] = {}
            items = s.find_all('div', class_='pi-item')
            for item in items:
                attr = item.find('h3', class_='pi-data-label')
                if attr is None:
                    attr = '<no attribute>'
                else:
                    attr = attr.text
                if attr == 'Species': is_character = True
                value = re.sub("[\(\[].*?[\)\]]" ,'', '], '.join(item.find('div', class_='pi-data-value').text.split(']')))
                value = value.strip()[:-1].replace(',,', ',')
                if ',' in value:
                    value = [i.strip() for i in value.split(',') if i.strip() != '']
                side_bar[title][attr] = value

        # Raw page content
        raw_content = soup.find('div', class_='mw-parser-output')
        if raw_content is not None:
            content_pgs = []
            for raw_paragraph in raw_content.find_all('p', recursive=False):
                if 'aside' in str(raw_paragraph): continue
                content_pgs.append(re.sub("[\(\[].*?[\)\]]" ,'', raw_paragraph.text) )
            # paragraph = value = re.sub("[\(\[].*?[\)\]]" ,'', raw_paragraph.text)


        else:
            # Empty page
            paragraph = ''

        # Data object
        scraped[page_url] = {
            'url': page_url,
            'title': heading,
            'is_character': is_character,
            'side_bar': side_bar,
            'paragraph': content_pgs
        }

    except:
        print(f'Failed! {page_url}')


# Save final part to disk
fn =  '../cache/starwars_small_canon_data.pickle'
with open(fn, 'wb') as f:
    pickle.dump(scraped, f, protocol=pickle.HIGHEST_PROTOCOL)

# 
## Let's do a quick test to make sure it worked we. Even if the data is big
## we can chunk it up with the above code and load it in sections.



bookFilePath = "../cache/starwars_*_canon_data*.pickle"
files = sorted(Path('.').glob(bookFilePath))
for fn in files:
  with open(fn,'rb') as f:
      part = pickle.load(f)
      for key, value in part.items():
          title = value['title'].strip()
          print(title)

########
# # Using LangChain to generate vectors and store in Elasticsearch
# 
# First we'll create the embeddings model

# 


def setup_embeddings():
    # Huggingface embedding setup
    print(">> Prep. Huggingface embedding setup")
    model_name = "sentence-transformers/all-mpnet-base-v2"
    return HuggingFaceEmbeddings(model_name=model_name)

hf = setup_embeddings()


########
# Next we'll create our elasticsearch vectorstore in the langchain style:

# 


index_name = "book_wookieepedia_small"

db = ElasticVectorSearch(embedding=hf,elasticsearch_url=es_url, index_name=index_name)



########
# Here goes the load. I like how small the code is, but eventually I'd love to see more flexibility on how we model the data as I'd like to do more hybrid search techniques.

#


count = 0
bookFilePath = "../cache/starwars_*_canon_data*.pickle"
files = sorted(Path('.').glob(bookFilePath))
batchtext = []



for fn in files:
    print(f"Starting book: {fn}")
    with open(fn,'rb') as f:
        part = pickle.load(f)

        for ix, (key, value) in tqdm(enumerate(part.items()), total=len(part)):
            paragraphs = value['paragraph']
            for px, p in enumerate(paragraphs):
                # print(f"{ix} {px} {title}")
                batchtext.append(p)
                count = count + 1

print("")
print(len(batchtext))
db.from_texts(batchtext, embedding=hf, elasticsearch_url=es_url, index_name=index_name)



