# Semester Week 12 Progress Report

## Completed Work

- Added reusable Python math functions. They make whole-number addition problems at three difficulty levels. They also make fraction addition problems. They use `Fraction` to compare answers exactly.
- Added three LLM-selectable tools: `create_math_problem`, `create_fraction_problem`, and `verify_math_answer`.
- The project author reported real tool-calling demonstrations during development. These demonstrations were not run again when this report was written. This report does not include a saved end-to-end trace for the updated schemas.
- Added a typed, immutable `ProblemRecord`. Its fields cannot be changed after creation. Added a small in-memory `ProblemStore`. Each new problem has a unique `problem_id`. Public tool results do not include the stored correct answer.
- Changed answer verification. It accepts only `problem_id` and `student_answer`. The app gets the correct answer from its store. A strict Pydantic schema rejects extra arguments, such as `correct_answer`.
- Ran `.venv/bin/python -m pytest -q` after the storage and verification changes. Result: **20 tests passed in 0.11 seconds**. These were local Python tests. They did not make OpenAI API calls.
- Improved the system prompt. It tells the model to use the same `problem_id` when it checks an answer. It tells the model not to invent IDs or invent or send `correct_answer`. After this change, a local syntax check of `src/tool_agent.py` returned `Syntax OK`. This check did not run the agent.

## Important Commits

- `f4c4fa1` — Add math tools and automated tests.
- `4f77a98` — Add fraction problems and guardrail tests.

These commit hashes and titles were checked in local Git history. The first version of this report did not list a commit for the new problem-store and prompt changes. These changes are now in commit `e49679c02c015301ce3206bd92f0d1e4c4d05df7` — Complete Week 12 math tutor progress and secure verification.

## Current Functionality

- The app returns structured dictionaries for whole-number addition and fraction addition problems.
- The LLM can select all three tools through `create_agent` in `src/tool_agent.py`.
- The app stores each problem and its correct answer in memory. It returns only the public problem fields to the caller.
- It checks answers against the stored correct answer. It accepts equivalent fractions, such as `6/8` and `3/4`.
- It returns a clear result for an unknown problem ID. The verification tool rejects a correct answer sent by the caller.
- There are 10 existing math tests and 10 new test cases. They check storage, verification, schema rules, private outputs, and unique IDs.

The store works only in the current process. The app does not yet have persistent student progress, adaptive difficulty, or a full multi-turn autonomous tutor workflow. The 20 passing tests do not cover all Advanced-track guardrail requirements.

## Problems Encountered

- The old verification tool accepted `correct_answer` from the LLM. The model could send a wrong correct answer. This could make the check wrong.
- The old problem result included the correct answer. The model could see it before the student answered.
- The old prompt did not explain how to use the same problem in a later answer check.
- Local tool tests do not show live LLM tool selection. They also do not show that the agent keeps the chat history across separate requests.

## Solutions

- Kept the math functions reusable. Moved the correct answer into a store controlled by the app.
- Added a public view of each problem. It does not include `correct_answer`. The record's default representation also hides the correct answer.
- Added strict verification arguments. Added tests to show that the tool rejects a supplied `correct_answer`. This argument cannot replace the stored answer.
- Updated the prompt to explain verification with `problem_id`.
- Used a separate in-memory store for each test. Reported local checks separately from API demonstrations.

## What I Learned

- The LLM can select tools. App code must control trusted data and check tool arguments.
- A problem ID links a new problem to its answer check. The LLM does not need to send the correct answer.
- Exact rational arithmetic helps compare equivalent fractions correctly.
- Schema validation and private tool outputs protect the app through code. Prompt instructions alone are not enough.
- Unit tests, syntax checks, and real model demonstrations show different things. Reports must explain them separately.

## Next Week

These are future plans. They are not completed features.

- Save a demonstration of tool selection with the updated schemas. Generate a problem, then check an answer with the same `problem_id`.
- Add agent-level error handling for invalid difficulty values and failed tools.
- Plan student state for each session and progress tracking. Add persistence and adaptive difficulty in later stages.
- Add execution limits, clear stopping reasons, and structured traces for the Advanced workflow.
- Add the four required Advanced guardrail scenarios: prompt injection, repeated tool failure, unauthorized or unapproved actions, and execution-limit termination.
- Write Python setup instructions. Add the app tests to CI.
