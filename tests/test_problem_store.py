from fractions import Fraction

import pytest
from pydantic import ValidationError

from src import agent
from src.problem_store import ProblemRecord, ProblemStore


@pytest.fixture
def store(monkeypatch):
    # Для каждого теста используем независимое хранилище без API.
    store = ProblemStore()
    monkeypatch.setattr(agent, "_problem_store", store)
    return store


def test_stored_correct_answer(store):
    problem = store.add(question="2 + 3 = ?", correct_answer="5", topic="whole_numbers")
    result = agent.verify_math_answer.invoke(
        {"problem_id": problem["problem_id"], "student_answer": "5"}
    )
    assert result["is_correct"] is True


def test_incorrect_answer_uses_stored_reference(store):
    problem = store.add(question="2 + 3 = ?", correct_answer="5", topic="whole_numbers")
    assert store.verify(problem["problem_id"], "6")["is_correct"] is False


def test_equivalent_fraction_answer(store):
    problem = store.add(question="1/4 + 1/2 = ?", correct_answer="3/4", topic="fractions")
    assert agent.verify_math_answer.invoke(
        {"problem_id": problem["problem_id"], "student_answer": "6/8"}
    )["is_correct"] is True


def test_unknown_problem_id(store):
    assert agent.verify_math_answer.invoke(
        {"problem_id": "unknown", "student_answer": "5"}
    ) == {"is_correct": False, "message": "Unknown problem ID."}


def test_llm_cannot_supply_correct_answer(store):
    problem = store.add(question="2 + 3 = ?", correct_answer="5", topic="whole_numbers")
    with pytest.raises(ValidationError):
        agent.verify_math_answer.invoke({
            "problem_id": problem["problem_id"],
            "student_answer": "6",
            "correct_answer": "6",
        })
    assert store.verify(problem["problem_id"], "6")["is_correct"] is False


def test_verification_schema_exposes_only_public_arguments():
    schema = agent.verify_math_answer.args_schema.model_json_schema()
    assert set(schema["properties"]) == {"problem_id", "student_answer"}
    assert schema["additionalProperties"] is False


@pytest.mark.parametrize("tool", [agent.create_math_problem, agent.create_fraction_problem])
def test_generated_problem_is_private_and_verifiable(store, tool):
    problem = tool.invoke({})
    assert "correct_answer" not in problem
    assert set(problem) <= {"problem_id", "question", "topic", "difficulty"}
    left, right = problem["question"].removesuffix(" = ?").split(" + ")
    answer = str(Fraction(left) + Fraction(right))
    assert agent.verify_math_answer.invoke(
        {"problem_id": problem["problem_id"], "student_answer": answer}
    )["is_correct"] is True


def test_generated_problems_have_unique_ids(store):
    first = agent.create_math_problem.invoke({})
    second = agent.create_math_problem.invoke({})
    assert first["problem_id"] != second["problem_id"]


def test_record_repr_hides_correct_answer():
    record = ProblemRecord("id", "question", "private-reference", "fractions")
    assert "private-reference" not in repr(record)
    assert "correct_answer" not in record.public_view()
