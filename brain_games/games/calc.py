import random

DESCRIPTION = 'What is the result of the expression?'

OPERATIONS = ('+', '-', '*')

MIN_NUMBER = 1
MAX_NUMBER = 100


def apply_operation(first, second, operation):
    match operation:
        case '+':
            return first + second
        case '-':
            return first - second
        case '*':
            return first * second


def generate_round():
    first = random.randint(MIN_NUMBER, MAX_NUMBER)
    second = random.randint(MIN_NUMBER, MAX_NUMBER)
    operation = random.choice(OPERATIONS)
    question = f'{first} {operation} {second}'
    answer = str(apply_operation(first, second, operation))
    return question, answer
