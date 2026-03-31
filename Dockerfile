FROM --platform=linux/arm64 python:3.13-slim

RUN dpkg --configure -a \
  && apt-get clean \
  && apt-get update \
  && apt-get install -y --no-install-recommends build-essential curl \
  && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /app/
COPY ./client/ /app/

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["uwsgi", "app.ini"]