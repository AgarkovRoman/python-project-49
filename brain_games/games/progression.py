import random

DESCRIPTION = 'What number is missing in the progression?'

MIN_LENGTH = 5
MAX_LENGTH = 10
HIDDEN_SYMBOL = '..'


def build_sequence(start, step, length):
    return [start + index * step for index in range(length)]


def generate_round():
    length = random.randint(MIN_LENGTH, MAX_LENGTH)
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    sequence = build_sequence(start, step, length)
    hidden_index = random.randint(0, length - 1)
    answer = str(sequence[hidden_index])
    displayed = [
        HIDDEN_SYMBOL if index == hidden_index else str(number)
        for index, number in enumerate(sequence)
    ]
    question = ' '.join(displayed)
    return question, answer
