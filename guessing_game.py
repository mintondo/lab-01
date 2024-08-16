import random


def guessing_game():
    print("Welcome to the Guessing Game!")
    number_to_guess = random.randint(1, 25)
    guess = None

    while guess != number_to_guess:
        guess = int(input("Guess a number between 1 and 25: "))

        if guess < number_to_guess:
            print("Higher!")
        elif guess > number_to_guess:
            print("Lower!")
        else:
            print("Congratulations! You guessed the correct number.")


if __name__ == '__main__':
    guessing_game()
