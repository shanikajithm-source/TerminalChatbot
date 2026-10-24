
from datetime import datetime
from difflib import get_close_matches
import random

print("================================")
print("       TERMINAL CHATBOT")
print("================================")

print("Bot: Hello! I am your Python chatbot.")

name = input("Bot: What is your name? ").strip()

if name == "":
    name = "Friend"

print("Bot: Nice to meet you,", name)
print("Bot: Type 'help' to see what I can do.")
print("Bot: Type 'bye' to exit.")

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the computer go to the doctor? It had a virus!",
    "Why was the Python programmer calm? Because they handled exceptions!",
    "Why do Python programmers wear glasses? Because they can't C!"
]

# Messages the chatbot understands
commands = {
    "hi": "greeting",
    "hii": "greeting",
    "hiii": "greeting",
    "hello": "greeting",
    "helloo": "greeting",
    "hey": "greeting",
    "heyy": "greeting",
    "heyyy": "greeting",

    "how are you": "feeling",
    "how are u": "feeling",
    "how r u": "feeling",
    "how are you doing": "feeling",

    "what is your name": "identity",
    "who are you": "identity",
    "your name": "identity",

    "time": "time",
    "what is the time": "time",
    "current time": "time",

    "date": "date",
    "what is the date": "date",
    "today's date": "date",
    "current date": "date",

    "joke": "joke",
    "tell me a joke": "joke",
    "make me laugh": "joke",

    "thanks": "thanks",
    "thank you": "thanks",
    "thank u": "thanks",
    "thx": "thanks",

    "help": "help",

    "bye": "exit",
    "exit": "exit",
    "quit": "exit"
}

while True:

    message = input("\nYou: ").strip().lower()

    if message == "":
        print("Bot: Please type a message.")
        continue

    # First check for an exact match
    if message in commands:
        intent = commands[message]

    else:
        # Try to find a similar command
        matches = get_close_matches(
            message,
            commands.keys(),
            n=1,
            cutoff=0.7
        )

        if matches:
            matched_message = matches[0]
            print("Bot: Did you mean '" + matched_message + "'?")

            confirmation = input("You (yes/no): ").strip().lower()

            if confirmation in ["yes", "y"]:
                intent = commands[matched_message]
            else:
                print("Bot: Okay! Type 'help' to see my commands.")
                continue

        else:
            print("Bot: Sorry, I don't understand that yet.")
            print("Bot: Type 'help' to see what I understand.")
            continue

    # Respond based on the identified intent
    if intent == "greeting":
        print("Bot: Hello,", name + "! How can I help you?")

    elif intent == "feeling":
        print("Bot: I am doing great! Thank you for asking.")

    elif intent == "identity":
        print("Bot: I am a Python Terminal Chatbot.")
        print("Bot: I was created using Python!")

    elif intent == "time":
        current_time = datetime.now().strftime("%I:%M %p")
        print("Bot: The current time is", current_time)

    elif intent == "date":
        current_date = datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's date is", current_date)

    elif intent == "joke":
        print("Bot:", random.choice(jokes))

    elif intent == "thanks":
        print("Bot: You're welcome,", name + "!")

    elif intent == "help":
        print("\n========== HELP MENU ==========")
        print("hi / hello / hey")
        print("how are you / how are u")
        print("what is your name")
        print("time")
        print("date")
        print("joke")
        print("thank you")
        print("bye / exit / quit")
        print("===============================")

    elif intent == "exit":
        print("Bot: Goodbye,", name + "! Have a nice day!")
        break
