from elasticsearch import Elasticsearch

client = Elasticsearch(
  "https://localhost:9200",
  basic_auth=("elastic", "changeme"), verify_certs=False
)

api_key="eXJnM2lZd0JqNy1QMGJHMWRnUUE6NWtuLWM1V3hSTDJ3T2Y1WE5aZFJmQQ==",

# API key should have cluster monitor rights
client.info()

documents = [
  { "index": { "_index": "search-t1", "_id": "9780553351927"}},
  {"name": "Snow Crash", "author": "Neal Stephenson", "release_date": "1992-06-01", "page_count": 470, "_extract_binary_content": True, "_reduce_whitespace": True, "_run_ml_inference": False},
  { "index": { "_index": "search-t1", "_id": "9780441017225"}},
  {"name": "Revelation Space", "author": "Alastair Reynolds", "release_date": "2000-03-15", "page_count": 585, "_extract_binary_content": True, "_reduce_whitespace": True, "_run_ml_inference": False},
  { "index": { "_index": "search-t1", "_id": "9780451524935"}},
  {"name": "1984", "author": "George Orwell", "release_date": "1985-06-01", "page_count": 328, "_extract_binary_content": True, "_reduce_whitespace": True, "_run_ml_inference": False},
  { "index": { "_index": "search-t1", "_id": "9781451673319"}},
  {"name": "Fahrenheit 451", "author": "Ray Bradbury", "release_date": "1953-10-15", "page_count": 227, "_extract_binary_content": True, "_reduce_whitespace": True, "_run_ml_inference": False},
  { "index": { "_index": "search-t1", "_id": "9780060850524"}},
  {"name": "Brave New World", "author": "Aldous Huxley", "release_date": "1932-06-01", "page_count": 268, "_extract_binary_content": True, "_reduce_whitespace": True, "_run_ml_inference": False},
  { "index": { "_index": "search-t1", "_id": "9780385490818"}},
  {"name": "The Handmaid's Tale", "author": "Margaret Atwood", "release_date": "1985-06-01", "page_count": 311, "_extract_binary_content": True, "_reduce_whitespace": True, "_run_ml_inference": False},
]

# client.bulk(operations=documents, pipeline="ent-search-generic-ingestion")


print(client.search(index="search-t1", q="snow"))