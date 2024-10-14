# Dockerfile to build the server part of the application as a docker image
# Optional - the server can be run locally via python

FROM python:3.10-slim

# Install system-level dependencies for grpcio
#RUN apt-get update && apt-get install -y \
#    tool1 \
#    tool2

WORKDIR /app_build

COPY . /app_build

# install the python dependcies, but cache libs between builds
RUN --mount=type=cache,target=/root/.cache \
    pip --timeout=1000 install -r requirements.txt 

#  poetry config virtualenvs.create false && \
#  poetry install --no-interaction --no-ansi --only main

# start server components of project on launch
#old
#CMD cd app && exec uvicorn app.server:app_build --host 0.0.0.0 --port 8001

# Run server.py from app  when the container launches
CMD cd app
ENTRYPOINT ["python", "server.py"]
