
import requests
import pprint as pprint

# from https://realpython.com/api-integration-in-python/
# https://www.datacamp.com/tutorial/making-http-requests-in-python
# https://requests.readthedocs.io/en/latest/


#TODO - refactor into config
#TODO - refactor into true client

# The API endpoint
url = "http://localhost:8000/test_email"

new_data = {
    "email": "this is some sample text that an email would be",
    "query": "query"
}

# A GET request to the API
response = requests.post(url,params=new_data)
print(response)

# Print the response
response_json = response.json()
print(response_json)

