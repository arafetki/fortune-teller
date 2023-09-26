import random


def generate_random_answer():

    # List of possible answers
    answers = ["yes", "no", "maybe"]

    # Generate a random answer
    random_answer = random.choice(answers)

    return random_answer
