from langserve import RemoteRunnable 
import requests

''''
Proxy help methods to invoke the chain (via proper server)
*OR* Direct local call in not available
'''

'''

'''

def do_server_check():
    '''
    Checks if the configured server gives a response, else starts local server
    '''
    requests.get("http://localhost:8001/")


def get_response() -> str:

    do_server_check()

    chain_endpoint = "http://localhost:8001/"
    chain = RemoteRunnable(chain_endpoint)
    response = chain.invoke({"topic":"Tell me a joke about Dublin"})

    return response


# simple code to run from command line
if __name__ == '__main__':

    

    print(get_response())