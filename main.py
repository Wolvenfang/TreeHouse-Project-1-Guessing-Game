import random


def game_intro():
    print("▼" * 40)
    print("Welcome to the Number Guessing game.")
    print("▲" * 40)
    user_name = input("What is your name? ")
    print(user_name + " pick a number between 1-10, we'll let you know if you are too high or low. Enjoy!")


def determine_high_score(high_score, guess):
    if high_score == 0:
        return guess
    if high_score > guess:
        high_score = guess
    return high_score


def input_manager():
    while True:
        user_input = input("Would you like to play? (Enter Yes/No)  ")
        if user_input.lower() == "yes" or user_input.lower() == "no":
            return user_input
        else:
            print(user_input + " is an invalid response, please select Yes or No")
            continue


def start_game():
    game_intro()

    secret_number = random.randint(1, 10)
    guesses = 0
    high_score = 0

    play_a_game = input_manager()
    while play_a_game.lower() == "yes":
        player_guess = input("Guess a number between 1 and 10: ")
        guesses += 1
        try:
            player_guess = int(player_guess)
            if player_guess <= 0:
                print("Please pick a number between 1 and 10.")
                continue
            elif player_guess > 10:
                print(str(player_guess) + " is not a valid response, please pick a number between 1 and 10.")
                continue
            pass
        except ValueError:
            print("That isn't a valid number. Please try again.")
            continue
        if player_guess == secret_number:
            high_score = determine_high_score(high_score, guesses)
            print("You guessed correctly!")
            print("It took you {} guesses.".format(guesses))
            print("The current high score is {}".format(high_score))
            play_a_game = input_manager()

            if play_a_game.lower() == 'no':
                print("Thanks for playing; have a good day.")
                break
            else:
                print("The current high score is {}".format(high_score))
                guesses = 0
                secret_number = random.randint(1, 10)
        elif player_guess < secret_number:
            print("Too low, try higher.")
            continue
        elif player_guess > secret_number:
            print("Too high, try lower.")
            continue


if __name__ == '__main__':
    start_game()
