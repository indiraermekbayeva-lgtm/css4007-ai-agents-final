from fractions import Fraction

import random


# Создаём математическое задание для ученика
def generate_problem(difficulty="easy"):
    if difficulty == "easy":
        # Простое сложение целых чисел
        a = random.randint(1, 10)
        b = random.randint(1, 10)

    elif difficulty == "medium":
        # Сложение более крупных чисел
        a = random.randint(10, 50)
        b = random.randint(10, 50)

    elif difficulty == "hard":
        # Сложение чисел до 100
        a = random.randint(50, 100)
        b = random.randint(50, 100)

    else:
        # Отклоняем неизвестный уровень сложности
        raise ValueError("Invalid difficulty level.")

    return {
        "question": f"{a} + {b} = ?",
        "correct_answer": str(a + b),
        "difficulty": difficulty
    }

# Проверяем математический ответ ученика
def check_answer(student_answer, correct_answer):
    try:
        # Преобразуем ответы в числа или дроби
        student_value = Fraction(student_answer)
        correct_value = Fraction(correct_answer)

        # Сравниваем значения
        if student_value == correct_value:
            return {
                "is_correct": True,
                "message": "Correct answer!"
            }
        else:
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

# Создаём задание на сложение дробей
def generate_fraction_problem():
    # Выбираем числители и знаменатели
    numerator1 = random.randint(1, 5)
    denominator1 = random.randint(2, 8)

    numerator2 = random.randint(1, 5)
    denominator2 = random.randint(2, 8)

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