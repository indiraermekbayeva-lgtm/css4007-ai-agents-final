import pytest
from fractions import Fraction
from src.math_tools import check_answer, generate_problem, generate_fraction_problem

# Проверяем правильный ответ
def test_correct_answer():
    result = check_answer("3/4", "3/4")
    assert result["is_correct"] is True

# Проверяем неправильный ответ
def test_incorrect_answer():
    result = check_answer("2/6", "3/4")
    assert result["is_correct"] is False

# Проверяем эквивалентные дроби
def test_equivalent_fractions():
    result = check_answer("6/8", "3/4")
    assert result["is_correct"] is True

# Проверяем некорректный ввод
def test_invalid_input():
    result = check_answer("abc", "3/4")
    assert result["message"] == "Invalid answer format."

# Проверяем генерацию простого задания
def test_generate_easy_problem():
    problem = generate_problem("easy")

    assert problem["difficulty"] == "easy"
    assert "+" in problem["question"]
    assert problem["correct_answer"].isdigit()

# Проверяем генерацию задания средней сложности
def test_generate_medium_problem():
    problem = generate_problem("medium")

    assert problem["difficulty"] == "medium"
    assert "+" in problem["question"]

# Проверяем генерацию сложного задания
def test_generate_hard_problem():
    problem = generate_problem("hard")

    assert problem["difficulty"] == "hard"
    assert "+" in problem["question"]

# Проверяем генерацию задания с дробями
def test_generate_fraction_problem():
    problem = generate_fraction_problem()

    assert problem["topic"] == "fractions"
    assert "+" in problem["question"]

    # Извлекаем дроби из задания
    expression = problem["question"].replace(" = ?", "")
    left, right = expression.split(" + ")

    # Проверяем, что вычисленный ответ правильный
    expected_answer = Fraction(left) + Fraction(right)

    assert Fraction(problem["correct_answer"]) == expected_answer

# Проверяем защиту от неизвестного уровня сложности
def test_invalid_difficulty():
    with pytest.raises(ValueError, match="Invalid difficulty level."):
        generate_problem("impossible")

# Проверяем, что генератор создаёт две правильные дроби
def test_fraction_problem_uses_proper_fractions():
    # Проверяем несколько случайных заданий
    for _ in range(100):
        problem = generate_fraction_problem()

        expression = problem["question"].replace(" = ?", "")
        left, right = expression.split(" + ")

        # Обе дроби должны быть больше нуля и меньше единицы
        assert 0 < Fraction(left) < 1
        assert 0 < Fraction(right) < 1