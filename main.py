import openai
from gradio_client import Client
import environ
from typing import Optional

# Загрузка переменных окружения из файла `.env`
env = environ.Env()
# environ.Env.read_env()

# Получение значений из .env
OPENAI_API_KEY: str = env('OPENAI_API_KEY')
QWEN_URL: str = env('QWEN_URL', default="https://qwen-qwen2-72b-instruct.hf.space/")
LLAMA_URL: str = env('LLAMA_URL', default="https://huggingface-projects-llama-3-2-3b-instruct.hf.space/")
# Словарь для хранения истории сообщений для каждого пользователя
history: dict[str, list[str]] = {}

# Функция для работы с OpenAI
def openai_predict(input_message: str, context: str = "") -> str:
    """Отправка запроса в OpenAI с учетом контекста"""
    try:
        openai.api_key = OPENAI_API_KEY
        # Формирование полного сообщения с учетом контекста
        full_prompt: str = context + "\nПользователь: " + input_message
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=full_prompt,
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Ошибка при взаимодействии с OpenAI: {str(e)}"

# Функция для работы с QWen API (Gradio)
def qwen_predict(input_message: str, context: str = " ") -> str:
    """Отправка запроса к модели QWen с учетом контекста"""
    try:
        client = Client(QWEN_URL)
        # Формирование полного сообщения с учетом контекста
        result = client.predict(
            input_message,
            [["None", "None"]],
            context,
            api_name="/model_chat"
        )
        return result[1][1][1]
    except Exception as e:
        return f"Ошибка при взаимодействии с QWen: {str(e)}"

# Функция для работы с LLama 3 API
def llama_predict(input_message: str, context: str = "") -> str:
    """Отправка запроса в LLama 3 с учетом контекста"""
    try:
        client = Client(LLAMA_URL)
        # Формирование полного сообщения с учетом контекста
        result = client.predict(
            message=context + "\nПользователь: " + input_message,
            max_new_tokens=1024,
            temperature=0.6,
            top_p=0.9,
            top_k=50,
            repetition_penalty=1.2,
            api_name="/chat"
        )
        return result
    except Exception as e:
        return f"Ошибка при взаимодействии с LLama 3: {str(e)}"

# Функция для выбора и выполнения запроса
def main() -> None:
    """Основная функция для выбора API и обработки запросов"""
    # Выбор API для использования
    print("Выберите API для взаимодействия:")
    print("1. OpenAI ChatGPT")
    print("2. QWen API (Gradio)")
    print("3. LLama 3 (Hugging Face)")
    choice: str = input("Введите номер (1, 2 или 3): ").strip()

    if choice == "1":
        print("Вы выбрали OpenAI ChatGPT.")
        selected_predict = openai_predict
    elif choice == "2":
        print("Вы выбрали QWen API (Gradio).")
        selected_predict = qwen_predict
    elif choice == "3":
        print("Вы выбрали LLama 3 (Hugging Face).")
        selected_predict = llama_predict
    else:
        print("Неверный выбор. Завершение работы.")
        return

    # Инициализация пустой истории для текущего пользователя
    user_id: Optional[str] = "user"
    history[user_id] = []

    print("Добро пожаловать! Введите свой запрос или введите 'exit' для выхода из программы.")

    while True:
        user_input: str = input("Ваш запрос: ")
        if user_input.lower() == 'exit':
            print("Выход из программы. Спасибо за использование!")
            break

        print("Обрабатываем ваш запрос, пожалуйста подождите...")

        # Получение контекста из истории сообщений
        context: str = " | ".join(history.get(user_id, []))
        context = "Твои предыдущие сообщения: " + context if context else ""

        # Получение ответа от выбранного API с учетом контекста
        answer: str = selected_predict(user_input, context)
        
        # Сохранение текущего запроса и ответа в историю
        history[user_id].append(f"Пользователь: {user_input}")
        history[user_id].append(f"Ответ: {answer}")

        print(f"Ответ: {answer}\n")

# Запуск основной функции
if __name__ == '__main__':
    main()
