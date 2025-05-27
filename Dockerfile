FROM python:3.11-slim

LABEL maintainer="Max"

# Установка зависимостей
RUN apt-get update && apt-get install -y \
    curl unzip gnupg2 xvfb wget \
    fonts-liberation libnss3 libxss1 libappindicator3-1 \
    libasound2 libatk-bridge2.0-0 libgtk-3-0 libgbm1 libvulkan1 xdg-utils \
    && rm -rf /var/lib/apt/lists/*

# Установка Chrome конкретной версии
ENV CHROME_VERSION 122.0.6261.111-1

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get update && \
    apt-get install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb

# Установка ChromeDriver под эту версию Chrome
ENV CHROMEDRIVER_VERSION 122.0.6261.111

RUN wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/${CHROMEDRIVER_VERSION}/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin/ && \
    chmod +x /usr/local/bin/chromedriver && \
    rm /tmp/chromedriver.zip

# Установка зависимостей Python
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копирование проекта
COPY . .

# Запуск тестов
ENTRYPOINT ["xvfb-run", "pytest"]()
