FROM ubuntu:20.04

WORKDIR /app

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        software-properties-common \
        gpg-agent && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        python3.14 \
        python3.14-dev \
        python3.14-distutils \
        curl \
        libpq-dev \
        unixodbc-dev \
        libsasl2-dev && \
    curl -sS https://bootstrap.pypa.io/get-pip.py | python3.14 && \
    rm -rf /var/lib/apt/lists/*

RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.14 1 && \
    update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.14 1

COPY requirements.txt /app/
RUN python -m pip install --no-cache-dir --upgrade pip && \
    python -m pip install --no-cache-dir -r requirements.txt

COPY client/ /app/

CMD ["uwsgi", "app.ini"]