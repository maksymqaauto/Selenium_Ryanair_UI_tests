FROM python:3.11-slim

# Обновление системы и установка зависимостей
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    gnupg \
    ca-certificates \
    fonts-liberation \
    libnss3 \
    libxss1 \
    libasound2 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libx11-xcb1 \
    libgtk-3-0 \
    libdrm2 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    libpango-1.0-0 \
    libxext6 \
    libxfixes3 \
    lsb-release \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*

# Установка Google Chrome (for testing)
RUN mkdir -p /opt/chrome && \
    wget -q https://storage.googleapis.com/chrome-for-testing-public/137.0.7151.55/linux64/chrome-linux64.zip && \
    unzip chrome-linux64.zip -d /opt/chrome && \
    rm chrome-linux64.zip && \
    ln -s /opt/chrome/chrome-linux64/chrome /usr/bin/google-chrome

# Установка ChromeDriver (соответствующей версии)
RUN wget -q https://storage.googleapis.com/chrome-for-testing-public/137.0.7151.55/linux64/chromedriver-linux64.zip && \
    unzip chromedriver-linux64.zip -d /usr/local/bin/ && \
    rm chromedriver-linux64.zip && \
    chmod +x /usr/local/bin/chromedriver-linux64/chromedriver && \
    ln -s /usr/local/bin/chromedriver-linux64/chromedriver /usr/bin/chromedriver

# Установка Allure
RUN wget -q https://github.com/allure-framework/allure2/releases/download/2.27.0/allure-2.27.0.tgz && \
    tar -zxvf allure-2.27.0.tgz -C /opt/ && \
    ln -s /opt/allure-2.27.0/bin/allure /usr/bin/allure && \
    rm allure-2.27.0.tgz

# Установка Python-зависимостей
WORKDIR /usr/workspace
COPY ./requirements.txt /usr/workspace
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . /usr/workspace

# Устанавливаем переменные среды (если нужно)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Команда по умолчанию (если нужна)
CMD ["pytest", "--alluredir=allure-results"]
