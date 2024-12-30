"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Veronika Svitakova
email: svitakovaveronika16@gmail.com
discord: veronikasvitakova_67296
"""

import random
import time

def generate_secret_number():
    """Vygeneruje tajné 4místné číslo, kde číslice jsou unikátní a nezačíná 0."""
    digits = list(range(1, 10))
    first_digit = random.choice(digits)
    digits.remove(first_digit)
    remaining_digits = random.sample(digits + [0], 3)
    return str(first_digit) + ''.join(map(str, remaining_digits))


def is_valid_guess(guess):
    """Zkontroluje správnost uživatelem zadaného čísla a případnou duplicitu číslic."""
    if len(guess) != 4 or not guess.isdigit():
        return False
    if guess[0] == '0':
        return False
    if len(set(guess)) != 4:
        return False
    return True


def evaluate_guess(secret, guess):
    """Vyhodnotí tipované číslo uživatele a vrátí počet bulls a cows."""
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(g in secret for g in guess) - bulls
    return bulls, cows


def print_bulls_and_cows(bulls, cows):
    """Vytiskne počet bulls a cows s ohledem na jednotné/množné číslo."""
    bulls_text = "bull" if bulls == 1 else "bulls"
    cows_text = "cow" if cows == 1 else "cows"
    print(f"{bulls} {bulls_text}, {cows} {cows_text}")


def give_feedback(guesses):
    """Poskytne zpětnou vazbu na základě počtu pokusů."""
    if guesses <= 5:
        return "amazing"
    elif guesses <= 10:
        return "average"
    else:
        return "not so good"


def bulls_and_cows_game():
    """Hlavní funkce hry."""
    print("Hi there!")
    print("-----------------------------------------------")
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-----------------------------------------------")

    secret_number = generate_secret_number()

    guesses = 0
    start_time = time.time()

    while True:
        guess = input("Enter a number:\n-----------------------------------------------\n>>> ")

        if not is_valid_guess(guess):
            print("Invalid input! Please enter a 4-digit number with unique digits that does not start with 0.")
            continue

        guesses += 1
        bulls, cows = evaluate_guess(secret_number, guess)
        print_bulls_and_cows(bulls, cows)

        if bulls == 4:
            end_time = time.time()
            elapsed_time = round(end_time - start_time)
            print(f"Correct, you've guessed the right number in {guesses} guesses!")
            print(f"It took you {elapsed_time} seconds.")
            print(f"That's {give_feedback(guesses)}!")
            break


if __name__ == "__main__":
    bulls_and_cows_game()
