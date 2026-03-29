FROM python:3.14-slim

WORKDIR /app

COPY ./pyproject.toml /app/
COPY ./uv.lock /app/

RUN pip install uv
RUN uv pip install --system .

CMD ["uwsgi", "app.ini"]