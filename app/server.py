from fastapi import FastAPI
from langserve import add_routes

from lang_server.chain_factory import get_chain

import logging


'''
Lang Serve server which makes Lang chain available via REST API
When run normally, it is available via http://localhost:8001/docs
'''

app = FastAPI(title="LangServe Knowledbase Example")

add_routes(app, get_chain())


# when called via command line
if __name__ == "__main__":
    import uvicorn

    logging.info("Started LangServe on http://localhost:8001")
    uvicorn.run(app, host="0.0.0.0", port=8001)
