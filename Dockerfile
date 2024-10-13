# Dockerfile to build the server part of the application as a docker image
# Optional - the server can be run locally via python

FROM python:3.11-slim

WORKDIR /app_build

COPY . /app_build

# install the python dependcies, but cache libs between builds
RUN --mount=type=cache,target=/root/.cache \
    pip install -r requirements.txt

#  poetry config virtualenvs.create false && \
#  poetry install --no-interaction --no-ansi --only main

# start server components of project on launch
CMD cd app && exec uvicorn app.server:app_build --host 0.0.0.0 --port 8001
