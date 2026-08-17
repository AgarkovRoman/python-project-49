import random

DESCRIPTION = 'What is the result of the expression?'

OPERATIONS = ('+', '-', '*')


def calculate(first, second, operation):
    match operation:
        case '+':
            return first + second
        case '-':
            return first - second
        case '*':
            return first * second


def generate_round():
    first = random.randint(1, 100)
    second = random.randint(1, 100)
    operation = random.choice(OPERATIONS)
    question = f'{first} {operation} {second}'
    answer = str(calculate(first, second, operation))
    return question, answer
