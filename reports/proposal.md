# Project Proposal — Semester Week 10

## Project Title

AI Math Tutor — Intelligent Mathematics Learning Agent

## Problem Description

Many school students have difficulties with mathematics. They often make mistakes and do not understand why their answers are wrong.

The goal of this project is to create an AI agent that helps students learn mathematics step by step.

The agent will check answers, identify mistakes, explain mathematical concepts, and give new exercises based on student progress.

The application will focus on basic mathematics for students in grades 5–6.

## Target Users

- School students in grades 5–6.
- Students who need extra mathematics practice.
- Teachers who want to support students with learning exercises.

## Selected Difficulty

A

The selected difficulty is A — Advanced.

The project will use an autonomous LLM agent with multiple tools, planning, state management, and guardrails.

## Expected Functionality

1. Generate mathematics exercises.
2. Check student answers.
3. Identify common mathematical mistakes.
4. Give explanations and hints.
5. Change task difficulty based on student performance.
6. Save and retrieve student progress.
7. Plan the next learning activity.
8. Handle invalid inputs and tool errors.
9. Stop execution when the learning goal is completed or an execution limit is reached.

## Proposed Functions

### 1. generate_problem(topic, difficulty)

- **Purpose:** Generate a mathematics problem.
- **Input:** Topic (string), difficulty (string).
- **Output:** A problem with its correct answer and explanation.
- **Dependencies:** Python, math problem templates.

### 2. check_answer(problem, student_answer)

- **Purpose:** Check whether the student's answer is correct.
- **Input:** Problem (dictionary), student answer (string).
- **Output:** Correctness result and error information.
- **Dependencies:** Python, mathematical validation functions.

### 3. get_student_progress(student_id)

- **Purpose:** Retrieve previous student results.
- **Input:** Student ID (string).
- **Output:** Student progress and learning history.
- **Dependencies:** Python, local JSON storage.

### 4. save_student_progress(student_id, result)

- **Purpose:** Save a new learning result.
- **Input:** Student ID and exercise result.
- **Output:** Save confirmation or error.
- **Dependencies:** Python, local JSON storage.

### 5. plan_next_activity(progress, learning_goal)

- **Purpose:** Choose the next learning activity.
- **Input:** Student progress and learning goal.
- **Output:** A learning plan with the next task.
- **Dependencies:** LLM, LangGraph, validated progress data.

### 6. explain_mistake(problem, student_answer)

- **Purpose:** Explain a student's mistake and provide a hint.
- **Input:** Problem and student answer.
- **Output:** A short explanation and learning hint.
- **Dependencies:** LLM API, prompt templates, answer validation.

## Proposed Agent Tools

The LLM agent will be able to select and call these tools:

1. **generate_problem:** Creates a new exercise when the student needs practice.
2. **check_answer:** Checks a submitted answer using mathematical logic.
3. **get_student_progress:** Reads previous learning results to support personalized decisions.
4. **save_student_progress:** Stores validated results after an exercise.

The agent will select tools based on the student's request and the current learning state.

Tool arguments will be validated before execution. The agent will not execute arbitrary code or access unauthorized files.

## Model Selection

- **Programming language:** Python.
- **Agent framework:** LangGraph.
- **LLM:** OpenAI GPT-4o-mini (proposed).
- **Integration:** OpenAI API using environment variables.
- **Data storage:** Local JSON files.

The API key will be stored in a `.env` file. The `.env` file will be excluded from GitHub using `.gitignore`.

The model may be changed if API access is unavailable.

## Architecture

The application will use the following workflow:

```text
Student Request
       |
       v
Input Validation
       |
       v
LangGraph Agent (LLM)
       |
       v
Planning and Tool Selection
       |
       v
+----------------------------+
| Agent Tools                |
|                            |
| 1. Generate Problem        |
| 2. Check Answer            |
| 3. Get Student Progress    |
| 4. Save Student Progress   |
+----------------------------+
       |
       v
Update Learning State
       |
       v
Evaluate Results
       |
       v
Continue or Stop
       |
       v
Final Explanation / New Task
```

The agent will have a maximum number of execution steps.

It will stop when the task is completed, a safety rule is triggered, or the execution limit is reached.

The agent will keep a short execution log without API keys or private reasoning.

## Example Requests

### Example 1

**Student:** "Give me five multiplication exercises for grade 5."

**Expected result:** The agent generates appropriate exercises.

### Example 2

**Student:** "Check my answer: 8 + 3 × 4 = 44."

**Expected result:** The agent identifies the incorrect order of operations and provides a hint.

### Example 3

**Student:** "I made three mistakes in fractions. Give me easier exercises."

**Expected result:** The agent checks learning progress and generates easier fraction exercises.

### Example 4

**Student:** "Show my progress and recommend what I should study next."

**Expected result:** The agent retrieves learning history and suggests the next learning activity.

## Evaluation Plan

The application will be tested using automated Python tests and manual demonstrations.

At least 12 application tests will be implemented.

### Functional Tests

1. Generate a valid mathematics problem.
2. Check a correct answer.
3. Check an incorrect answer.
4. Identify a common mathematical mistake.
5. Retrieve student progress.
6. Save student progress.
7. Select the correct tool.
8. Complete a multi-step learning task.

### Guardrail Tests

9. Reject an invalid or unauthorized file operation.
10. Reject a prompt injection attempting to bypass agent rules.
11. Stop when the maximum execution step limit is reached.
12. Handle a failed tool call without unsafe actions.

Additional tests will cover invalid model output and API failures.

The results will be recorded in the final report.

## Weekly Milestones

### Week 10 — November 2–8

- Select project topic and difficulty level.
- Define application requirements.
- Design the proposed functions and tools.
- Prepare the architecture.
- Complete the project proposal.

### Week 11 — November 9–15

- Set up the Python environment.
- Configure the LLM API.
- Implement the first working LLM request.
- Add basic documentation.

### Week 12 — November 16–22

- Implement mathematics problem generation.
- Implement answer checking.
- Add input and output validation.
- Create initial tests.

### Week 13 — November 23–29

- Implement agent tools.
- Register tools with the LLM.
- Demonstrate model-based tool selection.
- Add tool execution logging.

### Week 14 — November 30 – December 6

- Build the LangGraph workflow.
- Implement agent state and planning.
- Add difficulty adaptation.
- Define stopping conditions.
- Select a recent research paper.

### Week 15 — December 7–13

- Implement guardrails.
- Add execution limits.
- Handle tool failures.
- Test unauthorized actions and prompt injection.

### Week 16 — December 14–20

- Complete at least 12 tests.
- Evaluate agent performance.
- Fix errors.
- Prepare the research paper presentation.
- Complete documentation.

### Week 17 — December 21–22

- Complete the final report.
- Run the full test suite.
- Prepare the working demonstration.
- Submit the GitHub fork URL and final commit hash.
- Defend the project.

## AI Coding Assistant Disclosure

ChatGPT will be used to support project planning, code explanations, debugging, and documentation.

All generated code will be reviewed, tested, and explained by me.
