FROM python:3.11-alpine

# Установка Chrome и chromedriver
RUN apk update && apk add --no-cache \
    chromium \
    chromium-chromedriver \
    bash \
    curl \
    wget \
    openjdk11-jre \
    tar

# Установка Allure
RUN curl -o allure.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.8/allure-commandline-2.13.8.tgz && \
    tar -zxvf allure.tgz -C /opt/ && \
    ln -s /opt/allure-2.13.8/bin/allure /usr/bin/allure && \
    rm allure.tgz

WORKDIR /tests
COPY . /tests

RUN pip install --no-cache-dir -r requirements.txt
