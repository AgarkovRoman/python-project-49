import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'

MIN_NUMBER = 1
MAX_NUMBER = 100


def calculate_gcd(first, second):
    while second != 0:
        first, second = second, first % second
    return first


def generate_round():
    first = random.randint(MIN_NUMBER, MAX_NUMBER)
    second = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = f'{first} {second}'
    answer = str(calculate_gcd(first, second))
    return question, answer
