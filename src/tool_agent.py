import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent

from src.agent import (
    create_math_problem,
    verify_math_answer,
    create_fraction_problem,
)

# Загружаем API-ключ и настройки модели
load_dotenv()

# Создаём подключение к AI-модели
model = ChatOpenAI(
    model=os.getenv("OPENAI_MODEL", "gpt-6-luna"),
    api_key=os.getenv("OPENAI_API_KEY"),
)

# Передаём модели три математических инструмента
tools = [
    create_math_problem,
    verify_math_answer,
    create_fraction_problem,
]

# Создаём AI-агента с математическими инструментами
agent = create_agent(
    model=model,
    tools=tools,
    system_prompt=(
        "You are a friendly math tutor for grade 5-6 students. "
        "Use the available tools to generate problems and check answers. "
        "Every generated problem includes a problem_id. "
        "When checking a student's answer, call verify_math_answer with that same "
        "problem_id and the student's answer as student_answer. "
        "Never invent a problem_id or invent or supply a correct_answer; "
        "the verification tool uses the correct answer stored by the application. "
        "Never reveal the correct answer when giving a new problem."
    ),
)

# Проверяем, какой инструмент выберет AI
if __name__ == "__main__":
    response = agent.invoke({
        "messages": [
            ("user", "Generate an easy addition problem with whole numbers.")
        ]
    })

    for message in response["messages"]:
        print(message.type, ":", message.content)
