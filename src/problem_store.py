from dataclasses import dataclass, field
from uuid import uuid4

from src.math_tools import check_answer


@dataclass(frozen=True)
class ProblemRecord:
    problem_id: str
    question: str
    correct_answer: str = field(repr=False)
    topic: str
    difficulty: str | None = None

    def public_view(self) -> dict:
        # Возвращаем только разрешённые публичные поля.
        result = {
            "problem_id": self.problem_id,
            "question": self.question,
            "topic": self.topic,
        }
        if self.difficulty is not None:
            result["difficulty"] = self.difficulty
        return result


class ProblemStore:
    def __init__(self) -> None:
        self._problems: dict[str, ProblemRecord] = {}

    def add(
        self,
        *,
        question: str,
        correct_answer: str,
        topic: str,
        difficulty: str | None = None,
    ) -> dict:
        record = ProblemRecord(
            problem_id=str(uuid4()),
            question=question,
            correct_answer=correct_answer,
            topic=topic,
            difficulty=difficulty,
        )
        self._problems[record.problem_id] = record
        return record.public_view()

    def verify(self, problem_id: str, student_answer: str) -> dict:
        record = self._problems.get(problem_id)
        if record is None:
            return {"is_correct": False, "message": "Unknown problem ID."}
        # Эталон берём только из внутреннего хранилища.
        return check_answer(student_answer, record.correct_answer)
