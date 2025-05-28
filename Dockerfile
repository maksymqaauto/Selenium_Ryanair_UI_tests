FROM python:3.10-slim

# Установка зависимостей ОС
RUN apt-get update && apt-get install -y \
    wget curl unzip gnupg2 ca-certificates fonts-liberation libnss3 libxss1 libgconf-2-4 libasound2 libatk-bridge2.0-0 libgtk-3-0 \
    chromium chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /usr/src/app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем Python-зависимости
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копируем весь проект
COPY . .

# Создаём нужные директории
RUN mkdir -p logs screenshots allure-results

# Запускаем pytest при запуске контейнера
CMD ["pytest"]
