from fastapi import FastAPI
from langserve import add_routes

from lang_server.chain import get_chain

'''
Lange Server server which makes chain available via REST API
When run normally, it is available via http://localhost:8001/docs
'''

app = FastAPI(title="LangServe Launch Example")

add_routes(app, get_chain())

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001)
