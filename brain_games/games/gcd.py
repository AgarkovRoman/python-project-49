import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def calculate_gcd(first, second):
    while second != 0:
        first, second = second, first % second
    return first


def generate_round():
    first = random.randint(1, 100)
    second = random.randint(1, 100)
    question = f'{first} {second}'
    answer = str(calculate_gcd(first, second))
    return question, answer
