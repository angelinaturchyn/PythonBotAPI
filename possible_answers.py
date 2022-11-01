import random


def random_string():
    possible_answers = [
        "Didn't quite get that",
        "Can you paraphrase your question please?",
        "Do you mind trying again?"
    ]

    answers_count = len(possible_answers)
    random_answer = random.randrange(answers_count)

    return possible_answers[random_answer]
