import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True


def generate_round():
    number = random.randint(1, 100)
    answer = 'yes' if is_prime(number) else 'no'
    return str(number), answer
