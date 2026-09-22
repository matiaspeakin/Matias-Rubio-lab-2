import random


game_number = random.randint(1,10)
print(game_number)

while( True):

    user_guess = int(input("guess a number between 1 and 10: "))


    if user_guess > game_number:
        print("yo your stright booty but checks its too high")
    elif user_guess < game_number:
        print("yo your stright booty but checks its too low")
    else:
        print("good job you guessed the number")
        break