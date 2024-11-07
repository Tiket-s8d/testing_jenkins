# Используем базовый образ с установленным Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей и устанавливаем их
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Копируем все файлы проекта в контейнер
COPY . .

# Указываем команду для запуска приложения
CMD ["python", "main.py"]
