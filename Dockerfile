# Dockerfile to build the server part of the application as a docker image
# Optional - the server can be run locally via python

# to run this file
#docker build -t ragservice .

FROM python:3.10-slim

# Install system-level dependencies for grpcio
#RUN apt-get update && apt-get install -y \
#    tool1 \
#    tool2

EXPOSE 8001

RUN pip install --upgrade pip

WORKDIR /app_build

# install the python dependcies, but cache libs between builds
COPY snapshot-requirements.txt ./

RUN --mount=type=cache,target=/root/.cache \
    pip --timeout=1000 --no-cache-dir install -r snapshot-requirements.txt 

COPY . /app_build
    


#  poetry config virtualenvs.create false && \
#  poetry install --no-interaction --no-ansi --only main

# start server components of project on launch
#old
#CMD cd app && exec uvicorn app.server:app_build --host 0.0.0.0 --port 8001

# Run server.py from app  when the container launches
CMD cd app
ENTRYPOINT ["python", "server.py"]
