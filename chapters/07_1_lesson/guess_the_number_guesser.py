# Number Guessing Game - Guesser
# The user thinks of a number between 1 and 100 and the program tries to guess it.
# The user should tell the program if the guess is too high, too low, or correct.
# The program should tell the user how many guesses it took to guess the number.

import random
MAX_NUMBER = 100
MIN_NUMBER = 1


def get_number_feedback():
    # TODO: Implement this function
    answer = input("enter 'h' if the guess is too high, 'l' if it's too low, c it's correct.")
    return answer


def get_number():
    # TODO: Implement this function
    return (MIN_NUMBER, MAX_NUMBER) // 2


def play_guesser():


    print('-' * 60)
    print()
    print(f"Think of a number between {MIN_NUMBER} and {MAX_NUMBER} (inclusive).")
    input("Press Enter when you have thought of a number yay play time😊.")
    print()
    guess_count = 0
    # TODO: Implement the rest of this function
    while True:
         guess_count += 1
         guess= get_number()
         print(f"i'm guessing{guess}")
         feedback=get_number_feedback()
         if feedback == 'c':
             print(f"i guessed your number in {guess_count} guesses")
             return guess_count
         elif feedback == 'h': 
             MAX_NUMBER == guess -1
         elif feedback == 'l': 
            MIN_NUMBER == guess +1
        


def main():
    print('-' * 60)
    print()
    print("Welcome to the Number Guessing Game!")
    print()
    while True:
        guess_count = play_guesser()
        answer = input("Do you want to play again? you better😜 (y/n) ").lower()
        if answer == "n":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()