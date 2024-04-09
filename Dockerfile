FROM ubuntu:22.04

RUN apt-get update && apt-get install --no-install-recommends -y \
    wget curl git nano build-essential python3-dev python3-venv python3-pip iputils-ping

RUN pip3 install --upgrade sentence-transformers langchain neo4j tiktoken pypdf pymupdf

SHELL [ "/bin/bash" ]
CMD [ "tail -f /dev/null" ]