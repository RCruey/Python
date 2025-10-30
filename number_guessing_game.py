import random

def numberGuessGame():

    number_to_guess = random.randrange(0, 101)
    number_of_guesses = 0 
    user_guess = None

    while user_guess != number_to_guess:
        number_of_guesses = number_of_guesses + 1
        print("Guess a number between 0 and 100:")

        user_guess = int(input(""))

        if user_guess > number_to_guess:
            print("Too high, try again!")
        elif user_guess < number_to_guess:
            print("Nope! Too low, try again.")
        
    print("Thats right! it was ", user_guess,".")
    print("would you like to play again?")

    play_again = input("")

    if play_again.lower() =="y":
        return True
    else:
        return False

while numberGuessGame():
    pass
   

print("Thanks for playing!")
