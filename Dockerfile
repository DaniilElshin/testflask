FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

COPY . /testflask
WORKDIR /testflask

RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["__init__.py"]