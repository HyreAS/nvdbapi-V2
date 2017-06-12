FROM python:3
MAINTAINER Bjorn-Olav Strand <bolav@ikke.no>

ENV DEBIAN_FRONTEND noninteractive
ENV TERM dumb

RUN apt-get update && apt-get install -y \
	python3-shapely

RUN pip install psycopg2 xmltodict shapely requests six pyproj

# docker build -t nvdbapi .
# docker run -v `pwd`:/mnt  -it nvdbapi /bin/bash
# docker run -it --rm --name my-running-script -v "$PWD":/usr/src/myapp -w /usr/src/myapp nvdbapi python bomstasjoner-retninger.py