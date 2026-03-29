FROM python:3.14-slim

WORKDIR /app

COPY ./client/ /app/
COPY ./requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["uwsgi", "app.ini"]