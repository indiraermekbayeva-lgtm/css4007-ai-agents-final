# Semester Week 13 Progress Report

November 23–29, 2026

## Completed Work

- I built a two-turn workflow for my AI Math Tutor.
- I added tool permissions, argument checks, and safe logs.
- I added short Russian comments to key Python functions and steps.
- All 39 Python tests and all 10 npm tests passed offline.
- I used Codex to help write and review the code, tests, and this report.

## Important Commits

- `Complete Week 13 tool integration and tests` adds the two-turn workflow, tool checks, safe logs, and offline tests.

## Current Functionality

On the first turn, the student asks for a problem. The LLM can choose `create_math_problem` for whole numbers or `create_fraction_problem` for fractions. The program saves the problem, its `problem_id`, and its private correct answer.

On the second turn, the student sends an answer. The LLM can call `verify_math_answer` with the ID of the current problem and the student's answer. The program checks the answer and shows the tool's message.

The real OpenAI demo worked. Both API requests returned HTTP 200.

1. The LLM chose `create_math_problem`. The program showed `5 + 4 = ?`.
2. The student entered `9`. The LLM chose `verify_math_answer`. The program showed `Correct answer!`.

## Problems Encountered

The program needed to know which problem the student was answering. A tool call from the LLM could also have a wrong ID, extra data, or a tool name that the program did not allow.

## Solutions

- The program keeps the current problem between turns. It checks that the tool gets the same `problem_id` and the student's answer.
- The program allows only the two problem tools on the first turn and only `verify_math_answer` on the second. It checks the arguments and allows at most one tool call per turn.
- The correct answer stays in the program. The logs show tool actions and results without saving answers or API keys.
- Offline tests check blocked calls, bad input, and what happens when a model or tool call fails.

## What I Learned

I learned how to keep the same problem across two turns. I also learned that the LLM can choose a tool, but the Python code must check the call before it runs.

## Next Week

I plan to improve how the tutor decides what to do after each tool result. I also plan to check when it stops and how it handles errors. I will choose a recent research paper for the A-level project.
