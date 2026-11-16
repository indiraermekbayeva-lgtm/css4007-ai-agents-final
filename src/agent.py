from langchain_core.tools import tool
from pydantic import BaseModel, ConfigDict

from src.math_tools import generate_problem, generate_fraction_problem
from src.problem_store import ProblemStore


_problem_store = ProblemStore()


class VerifyMathAnswerInput(BaseModel):
    # Запрещаем дополнительные аргументы, включая подмену эталона.
    model_config = ConfigDict(extra="forbid", strict=True)

    problem_id: str
    student_answer: str

# Делаем генератор заданий доступным для AI-агента
@tool
def create_math_problem(difficulty: str = "easy") -> dict:
    """Generate an addition problem for a student.

    Args:
        difficulty: Problem difficulty: easy, medium, or hard.
    """
    return _problem_store.add(topic="whole_numbers", **generate_problem(difficulty))

# Делаем проверку ответов доступной для AI-агента
@tool(args_schema=VerifyMathAnswerInput)
def verify_math_answer(problem_id: str, student_answer: str) -> dict:
    """Check whether a student's math answer is correct.

    Args:
        problem_id: The ID returned when the problem was generated.
        student_answer: The answer provided by the student.
    """
    return _problem_store.verify(problem_id, student_answer)

# Делаем генератор дробей доступным для AI-агента
@tool
def create_fraction_problem() -> dict:
    """Generate a fraction addition problem for a student."""
    return _problem_store.add(**generate_fraction_problem())

# Проверяем работу инструмента
if __name__ == "__main__":
    result = create_math_problem.invoke({"difficulty": "easy"})
    print(result)
    print(verify_math_answer.invoke({
        "student_answer": "2/4",
        "problem_id": result["problem_id"]
          }))
    print(create_fraction_problem.invoke({}))
