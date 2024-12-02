import random
import json
import time


def load_questions():
    with open("questions.json", "r") as f:
        questions = json.load(f)["questions"]

    return questions