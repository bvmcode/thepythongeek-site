FROM ubuntu:20.04

WORKDIR /app
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        ca-certificates \
        libssl-dev \
        zlib1g-dev \
        libbz2-dev \
        libreadline-dev \
        libsqlite3-dev \
        libncursesw5-dev \
        libffi-dev \
        liblzma-dev \
        tk-dev \
        uuid-dev \
        libgdbm-dev \
        libnss3-dev \
        libxml2-dev \
        libxmlsec1-dev \
        libpq-dev \
        unixodbc-dev \
        libsasl2-dev && \
    rm -rf /var/lib/apt/lists/*

RUN curl -fsSLO https://www.python.org/ftp/python/3.14.3/Python-3.14.3.tgz && \
    tar -xzf Python-3.14.3.tgz && \
    cd Python-3.14.3 && \
    ./configure --enable-optimizations --with-ensurepip=install && \
    make -j"$(nproc)" && \
    make altinstall && \
    cd / && rm -rf /app/Python-3.14.3 /app/Python-3.14.3.tgz

COPY requirements.txt .
RUN /usr/local/bin/python3.14 -m pip install --no-cache-dir --upgrade pip && \
    /usr/local/bin/python3.14 -m pip install --no-cache-dir -r requirements.txt

COPY client/ /app/

CMD ["uwsgi", "app.ini"]