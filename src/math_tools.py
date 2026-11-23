from fractions import Fraction

import random
import re


_EXPONENT = re.compile(r"[eE]([+-]?[\d_]+)\s*$")


# Создаём математическую задачу
def generate_problem(difficulty="easy"):
    if difficulty == "easy":
        a = random.randint(1, 10)
        b = random.randint(1, 10)

    elif difficulty == "medium":
        a = random.randint(10, 50)
        b = random.randint(10, 50)

    elif difficulty == "hard":
        a = random.randint(50, 100)
        b = random.randint(50, 100)

    else:
        raise ValueError("Invalid difficulty level.")

    return {
        "question": f"{a} + {b} = ?",
        "correct_answer": str(a + b),
        "difficulty": difficulty
    }


# Проверяем ответ ученика
def check_answer(student_answer, correct_answer):
    try:
        # Ограничиваем показатель степени перед преобразованием в Fraction
        exponent = _EXPONENT.search(student_answer) if isinstance(student_answer, str) else None
        if exponent and abs(int(exponent[1])) > 1000:
            return {"is_correct": False, "message": "Invalid answer format."}

        # Преобразуем ответы в числа или дроби
        student_value = Fraction(student_answer)
        correct_value = Fraction(correct_answer)

        # Сравниваем значения
        if student_value == correct_value:
            return {
                "is_correct": True,
                "message": "Correct answer!"
            }
        return {
            "is_correct": False,
            "message": "Incorrect answer. Try again!"
        }

    except (ValueError, ZeroDivisionError):
        # Обрабатываем некорректный ввод
        return {
            "is_correct": False,
            "message": "Invalid answer format."
        }


# Создаём задачу на сложение дробей
def generate_fraction_problem():
    # Выбираем знаменатели
    denominator1 = random.randint(2, 8)
    denominator2 = random.randint(2, 8)

    # Числитель всегда меньше знаменателя
    numerator1 = random.randint(1, denominator1 - 1)
    numerator2 = random.randint(1, denominator2 - 1)

    # Создаём дроби
    fraction1 = Fraction(numerator1, denominator1)
    fraction2 = Fraction(numerator2, denominator2)

    # Вычисляем правильный ответ
    correct_answer = fraction1 + fraction2

    return {
        "question": f"{fraction1} + {fraction2} = ?",
        "correct_answer": str(correct_answer),
        "topic": "fractions"
    }


# Проверяем инструмент на разных ответах ученика
if __name__ == "__main__":
    print(check_answer("2/6", "3/4"))
    print(check_answer("3/4", "3/4"))
    print(check_answer("6/8", "3/4"))
    print(check_answer("abc", "3/4"))
    print(generate_problem("easy"))
    print(generate_fraction_problem())
