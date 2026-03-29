FROM python:3.14-slim-bookworm

WORKDIR /app

RUN apt-get -o Acquire::Check-Valid-Until=false \
           -o Acquire::AllowInsecureRepositories=true \
           -o Acquire::AllowDowngradeToInsecureRepositories=true \
           update && \
    apt-get install -y --no-install-recommends --allow-unauthenticated \
        libpq-dev \
        unixodbc-dev \
        libsasl2-dev && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN python -m pip install --no-cache-dir --upgrade pip && \
    python -m pip install --no-cache-dir -r requirements.txt

COPY client/ /app/

CMD ["uwsgi", "app.ini"]