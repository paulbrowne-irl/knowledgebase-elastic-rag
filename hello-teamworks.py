import http.client

conn = http.client.HTTPSConnection("enterpriseireland2.eu.teamwork.com")


#Authorization': 'Bearer {{APIKEY}}'

payload = ''
headers = {
  'Authorization': 'Bearer twp_NlY5f1DfcOcLveQP9As05EstTw2r_eu'
}
conn.request("GET", "/desk/api/v2/tickets.json", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))


# curl -i https://enterpriseireland2.eu.teamwork.com/projects/api/v3/projects.json -H "Authorization: Basic twp_NlY5f1DfcOcLveQP9As05EstTw2r_eu"