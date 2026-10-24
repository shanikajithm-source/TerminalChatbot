# Python Terminal Chatbot

## Project Overview

A beginner-friendly, rule-based chatbot developed using Python. The chatbot communicates with users through the terminal, recognizes common messages, and suggests corrections for spelling mistakes.

## Features

- Interactive terminal-based conversation
- Personalized greetings
- Recognition of multiple greeting variations
- Responses to common questions
- Current date and time
- Random programming jokes
- Spelling suggestions using fuzzy matching
- User confirmation before accepting corrected messages
- Help menu displaying supported commands
- Graceful exit using `bye`, `exit`, or `quit`

## Technologies Used

- Python 3
- `datetime` — Date and time functionality
- `random` — Random joke selection
- `difflib` — Spelling similarity detection
- Visual Studio Code

## How to Run

**1. Clone the repository**

```bash
git clone https://github.com/shanikajithm-source/TerminalChatbot.git
```

**2. Open the project folder**

```bash
cd TerminalChatbot
```

**3. Run the chatbot**

```bash
python chatbot.py
```

No external Python packages are required.

## Sample Conversation

```text
Bot: Hello! I am your Python chatbot.
Bot: What is your name? Alex
Bot: Nice to meet you, Alex

You: hi
Bot: Hello, Alex! How can I help you?

You: jole
Bot: Did you mean 'joke'?
You (yes/no): yes
Bot: Why do programmers prefer dark mode? Because light attracts bugs!

You: bye
Bot: Goodbye, Alex! Have a nice day!
```

## How It Works

The chatbot uses a dictionary to associate recognized messages with response categories called intents.

When the user enters a message, the chatbot first checks for an exact match. If no exact match is found, Python's `difflib.get_close_matches()` searches for similar supported commands.

If a possible correction is found, the chatbot asks for confirmation before responding.

## Limitations

- The chatbot uses predefined rules rather than a generative AI model.
- It cannot understand unrestricted natural-language conversations.
- Spelling suggestions are based on text similarity and may occasionally be incorrect.

## Future Improvements

- Add more conversation topics.
- Improve sentence recognition.
- Save chat history.
- Add a graphical interface.
- Integrate an AI language model.

## Project Type

Python Internship Assignment — Terminal Chatbot