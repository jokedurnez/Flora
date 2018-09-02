FROM resin/rpi-raspbian:latest

MAINTAINER Joke Durnez <joke.durnez@gmail.com>

# Set the variables
ENV DEBIAN_FRONTEND noninteractive
ENV PYTHON_VERSION 3.6.0

WORKDIR /root
COPY requirements.txt /root/

# Install packages necessary for compiling python
RUN apt-get update && apt-get upgrade && apt-get install -y \
        build-essential \
        libncursesw5-dev \
        libgdbm-dev \
        libc6-dev \
        zlib1g-dev \
        libsqlite3-dev \
        tk-dev \
        libssl-dev \
        openssl \
        libbz2-dev

# Download and compile python
RUN apt-get install -y ca-certificates
ADD "https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz" /root/Python-${PYTHON_VERSION}.tgz
RUN tar zxvf "Python-${PYTHON_VERSION}.tgz" \
        && cd Python-${PYTHON_VERSION} \
        && ./configure \
        && make \
        && make install \
        && cd .. \
        && rm -rf "./Python-${PYTHON_VERSION}" \
        && rm "./Python-${PYTHON_VERSION}.tgz"

RUN apt-get install -y libncurses5-dev
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
