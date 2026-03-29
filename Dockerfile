FROM ubuntu:20.04

WORKDIR /app

ENV DEBIAN_FRONTEND=noninteractive

# Install build dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        libssl-dev \
        zlib1g-dev \
        libbz2-dev \
        libreadline-dev \
        libsqlite3-dev \
        libncursesw5-dev \
        libxml2-dev \
        libxmlsec1-dev \
        libffi-dev \
        liblzma-dev \
        libpq-dev \
        unixodbc-dev \
        libsasl2-dev \
        ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Build Python 3.14 from source
RUN curl -O https://www.python.org/ftp/python/3.14.0/Python-3.14.0a7.tgz && \
    tar -xzf Python-3.14.0a7.tgz && \
    cd Python-3.14.0a7 && \
    ./configure --with-ensurepip=install && \
    make -s -j$(nproc) && \
    make altinstall && \
    cd .. && \
    rm -rf Python-3.14.0a7 Python-3.14.0a7.tgz

# Set python3.14 as default
RUN update-alternatives --install /usr/bin/python python /usr/local/bin/python3.14 1 && \
    update-alternatives --install /usr/bin/python3 python3 /usr/local/bin/python3.14 1

COPY requirements.txt /app/
RUN python -m pip install --no-cache-dir --upgrade pip && \
    python -m pip install --no-cache-dir -r requirements.txt

COPY client/ /app/

CMD ["uwsgi", "app.ini"]