import http.client
import json
import logging
import pprint
import settings.token_loader as token_loader


'''
Lab to explore teamworks API
'''
logging.basicConfig(level=logging.INFO)

# Get API Key
# You can get a copy of this from https://[youraccount].eu.teamwork.com/desk/myprofile/apikeys
APIKEY = token_loader.setup_token("teamworks")
API_URL = token_loader.setup_token("api_url") #someinting like [your_account].eu.teamwork.com



#Setup connection
logging.info("Trying to connect to API:"+API_URL)
conn = http.client.HTTPSConnection(API_URL)
payload = ''
headers = {
  'Authorization': f'Bearer {APIKEY}'
}

#conn.request("GET", "/desk/api/v2/tickets.json", payload, headers)
#conn.request("GET", '/desk/api/v2/tickets.json?filter={"state":{"$in":["active","scheduled","merged","deleted"]}}', payload, headers)
conn.request("GET", '/desk/api/v2/tickets.json?filter={"agent":{"$in":["640138"]},"state":{"$in":["active"]}}', payload, headers)



res = conn.getresponse()
data = res.read()

j = json.loads(data)
print(type(j))
#pprint.pp(j['tickets'])
pprint.pp(j)
#print(data.decode("utf-8"))
#print(json.dumps(data.decode("utf-8")))

