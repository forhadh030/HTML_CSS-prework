import random

random_number = random.randint(1, 10)
guess = int(input("Guess a number 1-10: "))

if random_number == guess:
    print("You got it!")