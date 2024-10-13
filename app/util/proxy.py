from langserve import RemoteRunnable # pip install "langserve[client]"

''''
Proxy help methods to invoke the chain (via proper server)
*OR* Direct local call in not available
'''

chain_endpoint = "http://localhost:8001/"

chain = RemoteRunnable(chain_endpoint)

response = chain.invoke({"topic":"Tell me about NY"})

print(response)