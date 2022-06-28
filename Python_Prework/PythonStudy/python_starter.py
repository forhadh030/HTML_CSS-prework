import random
from re import I
'''
# GUESSING GAME

random_number = random.randint(1, 10)
guess = []

while random_number != guess:
    random_number = random.randint(1, 10)
    guess = int(input("Guess a number 1-10: "))
    if random_number == guess:
        print(f"Good Job! {random_number} is the number you guessed!")
    else:
        print(f"Unfortunately, the number is {random_number}, while your guess was {guess}")
'''
"""
def cleanWord(word):
    return word.replace('.', '').lower()

myString = "my name is Syed Hussain. I live in New York"
[[cleanWord(word) for word in sentence.split()] for sentence in myString.split('.')]

# How to turn tuple into dictionary
animalList = [("a", "aardvark"), ("b", "bear"), ("c", "cat"), ("d", "dog")]
animals = {item[0]: item[1] for item in animalList}
# animals = {key: value for key, value in animalList}

"""


function countSheeps(arrayOfSheep) {
  const present = arrayOfSheep.filter(sheep => sheep);
  return present.length;
}