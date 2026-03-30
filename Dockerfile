FROM ubuntu:20.04

RUN apt-get update \
  && apt-get install -y curl python3-pip python3-dev libpq-dev unixodbc-dev libsasl2-dev\
  && add-apt-repository ppa:deadsnakes/ppa \
  && apt-get update \
  && apt-get install -y python3.14 \
  && ln -s /usr/bin/python3.14 /usr/bin/python

COPY ./requirements.txt /app/
COPY ./client/ /app/

WORKDIR /app

RUN python3.14 -m pip install --upgrade pip
RUN python3.14 -m pip install -r requirements.txt

CMD ["uwsgi", "app.ini"]