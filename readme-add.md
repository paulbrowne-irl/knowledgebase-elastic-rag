

## update day to day run instrauciotns
* project root # in main
* docker compose up # background infranstucure
* cd app
* uvicorn service.service_email:app
* check running at
* open windows client

Notes that need moved into the mainbd readme.md

* Edit / move Bot piece of docs to labs

* service API docs addd
    http://localhost:8000/docs
    include image screenshot-api.png


## Confidentiality of info

* Info stored locally
* LLM (Lllama) runs locally
* information redacted (see setting in config file is you wish to turn this off)
* Even with these precautions, probably better to injest *only* emails that ahve gone externally - since these have some exposure to the internet


## troubleshooting
Additional spacy:
* python -m spacy download en_core_web_sm
* python -m spacy download en_core_web_sm

#TODO - how to download

pytest - from root 
python -m pytest
run individula test - update pytest section

## Vscode Setup
Note on extra settings from settings.json



# OLDER BRANCH - POSSIBLE REMOVE

* Note current snapshot of outlook plugin saved in GIST

## Outlook Extension - script lab

* Where to get from (link to Gist) - currently https://gist.github.com/paulbrowne-irl/dfe5e10bfe46182cf273217ae001b0de
* how to install scriptlab
* how to pin
* how to save (copy to clipboard - update Gitst)

## SSL Certs
* https://github.com/FiloSottile/mkcert
* https://dev.to/rajshirolkar/fastapi-over-https-for-development-on-windows-2p7d

## update start wtih ssl

OR uvicorn service.service_email:app 

## installing client only

* requirements-client.txt

