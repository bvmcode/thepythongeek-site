FROM python:3.11-slim

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
     gcc \
     unixodbc-dev \
     libsasl2-dev \
  && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /app/

WORKDIR /app

RUN pip install --upgrade pip \
  && pip install -r requirements.txt

COPY ./client/ /app/

CMD ["uwsgi", "app.ini"]