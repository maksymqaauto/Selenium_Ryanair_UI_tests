FROM python:3.11-slim

LABEL maintainer="Max"

# Установка зависимостей для Chrome и Selenium
RUN apt-get update && apt-get install -y \
    wget curl unzip gnupg2 xvfb \
    fonts-liberation libnss3 libxss1 libappindicator3-1 \
    libasound2 libatk-bridge2.0-0 libgtk-3-0 libgbm1 libvulkan1 xdg-utils \
    && rm -rf /var/lib/apt/lists/*

# Добавление репозитория Google Chrome и установка браузера
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && apt-get install -y google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*

# Создание рабочей директории
WORKDIR /app

# Копирование зависимостей и установка
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копирование всего проекта
COPY . .

# Запуск pytest при старте контейнера
ENTRYPOINT ["pytest"]


