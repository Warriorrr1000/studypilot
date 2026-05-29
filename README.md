# StudyPilot

#### Video Demo: https://youtu.be/rhzJenpLTDU?si=YqK5GDYg2xcSWV2H

#### Description:

StudyPilot is a terminal-based study environment made with Python as my final project for CS50’s Introduction to Programming with Python.

The idea behind this project was to create something actually useful instead of making a very small demo project with only one feature. I wanted to combine different study-related tools together in one place so it feels like a proper study assistant inside the terminal.

StudyPilot includes features like:

* AI question answering
* text summarization
* quiz generation
* flashcards
* revision tools
* study session tracking
* task management
* study statistics

This project is also an upgraded version of one of my older projects called "AI Study Companion". The previous version mostly focused on AI-based summaries and question answering, but this version is much more organized and has more features.

---

## Project Structure

```text
studypilot/
│
├── project.py
├── test_project.py
├── requirements.txt
├── README.md
├── LICENSE
│
├── api.py
├── config.py
├── ai_assistance.py
├── flashcards.py
├── revision.py
├── tasks.py
├── sessions.py
├── statistics.py
├── utils.py
│
└── data/
    ├── history.json
    ├── flashcards.json
    ├── revision.json
    ├── sessions.json
    └── tasks.json
```

---

## project.py

This is basically the main file of the project. It handles the menus, user interaction, and connects all the different modules together.

Instead of writing the entire project inside one huge file, I separated the main functionalities into different modules to make the code cleaner and easier to manage. So `project.py` mainly works as the integration layer of the application.

It also contains some helper functions used for menus, input validation, screen clearing, and error handling.

---

## api.py

This file handles the API requests for AI features using the `requests` library.

I used OpenRouter AI for this project. The `get_response()` function sends prompts to the AI model and returns the generated response.

I kept the API logic in a separate file so changing the AI provider or model later becomes easier.

---

## config.py

This file stores the API key separately from the main code.

I used this approach to avoid hardcoding sensitive information directly inside other files.

---

## ai_assistance.py

This module contains the main AI study features.

Functions included:

* `ask_question()`
* `summarize_text()`
* `generate_quiz()`
* `explain_topic()`
* `view_history()`

This module allows users to ask questions, generate quizzes, summarize text, and explain topics in simpler language.

The generated responses are also saved into JSON history files.

---

## flashcards.py

This module handles flashcard generation and management.

Functions included:

* `generate_flashcards()`
* `view_flashcards()`
* `delete_flashcards()`

The flashcards are generated using AI and stored locally in JSON format.

---

## revision.py

This module focuses on revision-related features.

Functions included:

* `generate_quick_notes()`
* `extract_key_points()`
* `generate_revision_questions()`
* `view_revision_history()`

These tools help users revise topics quickly before study sessions or exams.

---

## tasks.py

This module works as a simple task management system inside the application.

Functions included:

* `add_task()`
* `view_task()`
* `mark_completed()`
* `delete_task()`
* `edit_task()`

System function:

* `load_task()`

I added this feature because I wanted the application to also help with productivity instead of only generating AI responses.

---

## sessions.py

This module tracks study sessions.

Functions included:

* `start_session()`
* `end_session()`
* `view_sessions()`

System function:

* `load_session()`

The session system stores study durations, timestamps, and session status using JSON files and Python’s `datetime` module.

One design decision i made was adding a restriction where users cannot start another session while one is already active.

---

## statistics.py

This module calculates statistics using the stored study session data.

Functions included:

* `get_total_study_time()`
* `total_sessions_count()`
* `get_session_status()`
* `get_average_session_time()`
* `get_longest_session()`
* `get_subject_wise_study_time()`

This feature was added to make the project feel more complete and useful for long-term studying.

---

## utils.py

This file contains helper functions used across multiple modules.

Functions included:

* `format_duration()`
* `average()`
* `save()`
* `load()`

Separating these reusable functions into a separate file helped reduce repeated code.

---

## test_project.py

This file contains tests written using `pytest`.

The tests mainly focus on important utility and validation functions since `project.py` mostly acts as an integration and menu-handling layer.

Some tested functions include:

* `validate_menu_choice()`
* `is_valid_int()`
* `format_duration()`
* `average()`

---

## Design Choices

One of the main design choices I made was using a modular structure instead of writing everything in one file. Since the project contains many features, separating them into different modules made the project easier to understand and maintain.

I also decided to use JSON files instead of databases because the project is terminal-based and relatively lightweight.

Another decision was keeping the project CLI-based instead of creating a graphical interface. I wanted to focus more on Python programming concepts, logic, APIs, modularity, and file handling.

---

## Libraries Used

The project uses:

* requests
* colorama
* pytest
* json
* os
* time
* datetime

---

## Setup

To use AI-powered features, add your own API key inside `config.py`:

```python
API_KEY = "YOUR_API_KEY_HERE"
```

---

## Final Thoughts

This project helped me practice many Python concepts together such as:

* APIs
* modular programming
* file handling
* JSON storage
* testing with pytest
* datetime handling
* CLI application design
* error handling

It also gave me experience working on a larger Python project with multiple connected modules instead of making small standalone scripts.

In the future, I may continue improving StudyPilot by adding more advanced statistics, better AI features, and possibly a graphical interface.
