import random
import json
import time


def load_questions():
    with open("questions.json", "r") as f:
        questions = json.load(f)["questions"]

    return questions

def get_random_questions(questions, num_questions):
    if num_questions > len(questions):
        num_questions = len(questions)

    random_questions = random.sample(questions, num_questions)
    return random_questions

