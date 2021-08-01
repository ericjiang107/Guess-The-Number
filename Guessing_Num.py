# Creation of guessing game
import random

class anothergame():
    def __init__(self):
        self.numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    def Number(self):
        random_num = random.choice(self.numbers)
        return random_num

# Testing computer randomizer
# testing = anothergame()
# print(testing.Number())

    def player(self):
        guess = int(input("Please enter a number between 0-15: "))
        print(f'The number you have chosen is: {guess}')
        return guess
    
# Testing player number
# testing = anothergame()
# testing.player()

    def check(self, random_num, guess):
        if guess != random_num:
            print(f'Sorry, your guess: ({guess}) is not correct')
        elif guess == random_num:
            print(f'Congradulations!, your guess: ({guess}) matches the computers of: ({random_num})')
    

    
def trial():
    start_trial = anothergame()
    while True:
        response = input("Please enter 's' to start, 'c' to continue or 'g' to give up or quit: ")
        if response.lower() == "s":
            x = start_trial.Number()
            y = start_trial.player()
            start_trial.check(x, y)
        elif response.lower() == "g":
            print(f"Thank you for playing!")
            break
        elif response.lower() == "c":
            y = start_trial.player()
            start_trial.check(x, y)
        else:
            print("Sorry, that is not a valid response, please try again")
trial() 