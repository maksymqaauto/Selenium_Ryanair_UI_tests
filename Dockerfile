FROM python:3.11-slim

LABEL maintainer="Max"

# Установка зависимостей
RUN apt-get update && apt-get install -y \
    curl unzip gnupg2 xvfb wget \
    fonts-liberation libnss3 libxss1 libappindicator3-1 \
    libasound2 libatk-bridge2.0-0 libgtk-3-0 libgbm1 libvulkan1 xdg-utils \
    && rm -rf /var/lib/apt/lists/*

# Установка Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb

# Установка ChromeDriver (версия 136.0.7103.113)
RUN wget -O /tmp/chromedriver.zip https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/136.0.7103.113/linux64/chromedriver-linux64.zip && \
    unzip /tmp/chromedriver.zip -d /tmp/ && \
    mv /tmp/chromedriver-linux64/chromedriver /usr/local/bin/ && \
    chmod +x /usr/local/bin/chromedriver && \
    rm -rf /tmp/*

# Установка рабочей директории
WORKDIR /app

# Установка зависимостей
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копируем проект
COPY . .

# Создание директорий
RUN mkdir -p /app/logs /app/screenshots /app/allure-results

# Установка переменных окружения
ENV PYTHONWARNINGS="ignore"

# Запуск тестов
ENTRYPOINT ["xvfb-run", "--server-args=-screen 0 1920x1080x24", "pytest", "--capture=tee-sys", "-v"]
