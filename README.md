# Проект: Консольное приложение для взаимодействия с нейросетями

Данный проект представляет собой консольное приложение на Python, которое позволяет пользователю вводить произвольные запросы, отправлять их в нейронные сети (ChatGPT, QWen или LLama) и получать ответы обратно в консоль.

## Структура проекта

```
/
  ├── main.py            # Основной скрипт для запуска консольного приложения 
  ├── Dockerfile         # Описание Docker-образа для контейнеризации приложения 
  ├── docker-compose.yml # Файл для управления контейнерами с помощью Docker Compose 
  ├── Pipfile            # Описание зависимостей проекта для использования pipenv
  ├── Pipfile.lock       # Зафиксированные версии зависимостей проекта
  ├── .gitignore         # Список файлов и папок, игнорируемых Git
  └── .env               # Переменные окружения (например, API ключи)
```


## 1. Запуск приложения

Приложение позволяет отправлять запросы в нейросети (ChatGPT, QWen, LLama) через API и получать ответы.

### Шаги для запуска:

1. Установите зависимости с помощью pipenv:

   ```bash
   pipenv install
   ```

2. Создайте файл .env и укажите необходимые переменные окружения. Пример содержимого .env:

    ```bash
    OPENAI_API_KEY=ваш_ключ_openai
    QWEN_URL=https://qwen-qwen2-72b-instruct.hf.space/
    LLAMA_URL=https://huggingface-projects-llama-3-2-3b-instruct.hf.space/
    ```

3. Запустите приложение:

    ```bash
    pipenv run python main.py
    ```

4. Приложение запустится и предложит выбрать нейросеть для взаимодействия. Введите запрос в консоль для отправки его в выбранную нейросеть.

    ```bash
    Выберите API для взаимодействия:
    1. OpenAI ChatGPT
    2. QWen API (Gradio)
    3. LLama 3 (Hugging Face)
    Введите номер (1, 2 или 3): 1
    Вы выбрали OpenAI ChatGPT.

    Ваш запрос: Какой сегодня день?
    Ответ: Сегодня день среды.
    ```

## 2. Запуск через Docker

Приложение может быть запущено в контейнере с помощью Docker.

### Шаги для запуска:

1. Соберите Docker-образ:

   ```bash
   docker-compose build
   ```

2. Запустите контейнер через Docker Compose:

    ```bash
    docker-compose run --rm app
    ```

3. После запуска контейнера приложение будет готово к приему запросов через консоль.

## 3. Переменные окружения

Для корректной работы с API нейросетей необходимо настроить файл .env с соответствующими переменными окружения. 

### Основные переменные:

   ```bash
    OPENAI_API_KEY — API ключ для доступа к OpenAI.
    QWEN_URL — URL-адрес для модели QWen через Gradio.
    LLAMA_URL — URL-адрес для модели LLama через Hugging Face.
   ```

## 4. Логирование и история запросов

Приложение сохраняет историю запросов и ответов в памяти для каждого пользователя, чтобы поддерживать контекст общения с нейросетью.
