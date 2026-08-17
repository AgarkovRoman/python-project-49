import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

MIN_NUMBER = 1
MAX_NUMBER = 100
MIN_PRIME = 2


def is_prime(number):
    if number < MIN_PRIME:
        return False
    for divisor in range(MIN_PRIME, number):
        if number % divisor == 0:
            return False
    return True


def generate_round():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    answer = 'yes' if is_prime(number) else 'no'
    return str(number), answer
