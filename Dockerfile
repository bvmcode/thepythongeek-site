FROM ubuntu:20.04

RUN apt-get update \
  && apt-get install -y curl python3-pip python3-dev libpq-dev unixodbc-dev libsasl2-dev\
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip 

COPY ./requirements.txt /app/
COPY ./client/ /app/

WORKDIR /app

RUN curl -LsSf https://astral.sh/uv/install.sh | sh
RUN uv python install 3.14
RUN python3.14 -m pip install --upgrade pip
RUN python3.14 -m pip install -r requirements.txt

CMD ["uwsgi", "app.ini"]