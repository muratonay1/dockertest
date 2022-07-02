FROM python:3.7.8
ADD . /
WORKDIR /
RUN pip install -r requirements.txt