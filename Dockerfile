FROM python:3.11-slim

# Установка нужных пакетов
RUN apt-get update && apt-get install -y \
    curl wget unzip \
    fonts-liberation libnss3 libatk1.0-0 libatk-bridge2.0-0 libcups2 libxss1 libgbm1 libasound2 \
    && rm -rf /var/lib/apt/lists/*

# Скачиваем Chrome для тестирования
RUN wget -q -O /tmp/chrome-linux64.zip "https://storage.googleapis.com/chrome-for-testing-public/137.0.7151.55/linux64/chrome-linux64.zip" && \
    unzip /tmp/chrome-linux64.zip -d /usr/local/bin/ && \
    rm /tmp/chrome-linux64.zip

# Скачиваем ChromeDriver той же версии
RUN wget -q -O /tmp/chromedriver-linux64.zip "https://storage.googleapis.com/chrome-for-testing-public/137.0.7151.55/linux64/chromedriver-linux64.zip" && \
    unzip /tmp/chromedriver-linux64.zip -d /usr/local/bin/ && \
    rm /tmp/chromedriver-linux64.zip

# Перемещаем chromedriver в /usr/local/bin/chromedriver и даем права на выполнение
RUN mv /usr/local/bin/chromedriver-linux64/chromedriver /usr/local/bin/chromedriver && \
    chmod +x /usr/local/bin/chromedriver

# (Опционально) Можно добавить PATH, если надо
ENV PATH="/usr/local/bin:${PATH}"

WORKDIR /usr/workspace

COPY ./requirements.txt /usr/workspace/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/workspace

CMD ["pytest", "--maxfail=1", "--disable-warnings", "-q"]
