import os
from dotenv import load_dotenv
from openai import OpenAI

# Загружаем настройки из файла .env
load_dotenv()

# Получаем API-ключ и название модели
api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("OPENAI_MODEL", "gpt-6-luna")

# Проверяем, указан ли API-ключ
if not api_key:
    print("Error: API key is not configured.")
else:
    client = OpenAI(api_key=api_key)

    # Отправляем простой тестовый запрос к ИИ-модели
    response = client.responses.create(
        model=model,
        instructions="You are a friendly math tutor for grade 5 students.",
        input="Explain what a fraction is in two simple sentences.",
        max_output_tokens=150,
    )

    print("AI Math Tutor:")
    print(response.output_text)