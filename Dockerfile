# Указываем базовый образ Python
FROM python:3.11

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Создаем пользователя с ограниченными правами
RUN useradd -m appuser

# Копируем только Pipfile и Pipfile.lock для установки зависимостей
COPY Pipfile Pipfile.lock ./

# Обновляем pip до последней версии
RUN pip install --upgrade pip

# Устанавливаем pipenv и зависимости под новым пользователем
RUN pip install pipenv && pipenv install --system --deploy

# Копируем исходный код приложения в контейнер
COPY . /app

# Меняем владельца папки на созданного пользователя
RUN chown -R appuser:appuser /app

# Переключаемся на пользователя с ограниченными правами
USER appuser

# Запуск основного скрипта
CMD ["python", "main.py"]
