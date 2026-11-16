from src.math_tools import check_answer, generate_problem

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