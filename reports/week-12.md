# Semester Week 12 Progress Report

## Completed Work

- Implemented reusable Python functions for whole-number addition problems at three difficulty levels, fraction addition problems, and exact answer comparison using `Fraction`.
- Registered three LLM-selectable tools: `create_math_problem`, `create_fraction_problem`, and `verify_math_answer`.
- Completed manual real tool-calling demonstrations during development, as reported by the project author. These demonstrations were not rerun during report preparation, and this report does not claim a captured end-to-end trace for the updated schemas.
- Added a typed, immutable `ProblemRecord` and a small in-memory `ProblemStore`. Generated problems receive unique `problem_id` values; public tool results exclude the stored correct answer.
- Changed verification to accept only `problem_id` and `student_answer`. The application retrieves the reference answer from its store; a strict Pydantic schema rejects additional arguments such as `correct_answer`.
- Ran `.venv/bin/python -m pytest -q` after the storage and verification changes: **20 tests passed in 0.11 seconds**. These were local Python tests without OpenAI API calls.
- Improved the system prompt to require reuse of the generated `problem_id` and prohibit inventing IDs or inventing or supplying `correct_answer`. A subsequent local syntax check of `src/tool_agent.py` returned `Syntax OK`; the agent was not executed for that check.

## Important Commits

- `f4c4fa1` — Add math tools and automated tests.
- `4f77a98` — Add fraction problems and guardrail tests.

These commit hashes and titles were checked in local Git history. No commit hash is assigned here to the newer problem-store and prompt changes.

## Current Functionality

- Generates structured problem dictionaries for whole-number addition and fraction addition.
- Exposes all three tools to the LLM through `create_agent` in `src/tool_agent.py`.
- Stores each generated problem and its reference answer in memory, returning only public problem fields to the caller.
- Checks answers against the stored reference and recognizes equivalent fractions, such as `6/8` and `3/4`.
- Returns a controlled result for unknown problem IDs and rejects attempts to supply a reference answer through the verification tool.
- Includes 10 existing mathematical tests and 10 additional test cases covering storage, verification, schema restrictions, private outputs, and unique IDs.

The store lasts only for the current process. Persistent student progress, adaptive difficulty, and a complete multi-turn autonomous tutor workflow are not implemented. The 20 passing tests do not establish completion of all Advanced-track guardrail requirements.

## Problems Encountered

- The previous verification interface accepted `correct_answer` from the LLM, so an incorrect reference could produce an unreliable assessment.
- Returning the reference answer in a generated problem exposed it to the model before the student answered.
- The original prompt did not explain how to connect a generated problem to a later verification call.
- Automated local tool tests do not demonstrate live LLM selection or conversation continuity across separate requests.

## Solutions

- Kept the existing mathematical functions reusable and moved reference-answer ownership into an application-controlled store.
- Added an explicit public representation of each problem, excluding `correct_answer`, and hid the reference answer from the record's default representation.
- Added strict verification arguments and tests showing that a supplied `correct_answer` is rejected and cannot replace the stored reference.
- Updated the prompt to describe the new ID-based verification contract.
- Used isolated in-memory stores in tests and kept local checks separate from API demonstrations.

## What I Learned

- The LLM should select tools, while application code should control trusted reference data and enforce argument validation.
- A problem ID links generation and verification without sending the reference answer back through the LLM.
- Exact rational arithmetic supports reliable comparison of equivalent fractions.
- Schema validation and private tool outputs provide enforceable protections beyond prompt instructions.
- Unit tests, syntax checks, and real model demonstrations provide different evidence and should be reported separately.

## Next Week

- Add a documented demonstration of tool selection using the updated schemas, including generation followed by verification with the same `problem_id`.
- Add explicit handling for invalid difficulty values and tool failures at the agent boundary.
- Plan session-scoped student state and progress tracking; add persistence and adaptive difficulty in later implementation stages.
- Develop execution limits, stopping reasons, and structured traces for the Advanced workflow.
- Add the four mandatory Advanced guardrail scenarios: prompt injection, repeated tool failure, unauthorized or unapproved actions, and execution-limit termination.
- Document Python setup and connect the application tests to CI. These items are future work, not completed features.
