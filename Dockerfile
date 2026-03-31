FROM python:3.13-slim

RUN apt-get update \
  && apt-get install -y curl libpq-dev unixodbc-dev libsasl2-dev \
  && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /app/
COPY ./client/ /app/

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["uwsgi", "app.ini"]