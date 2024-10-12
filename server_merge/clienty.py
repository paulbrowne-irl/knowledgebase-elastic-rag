from langserve import RemoteRunnable # pip install "langserve[client]"

chain_endpoint = "http://localhost:8001/"

chain = RemoteRunnable(chain_endpoint)

response = chain.invoke({"topic":"Tell me about NY"})

print(response)