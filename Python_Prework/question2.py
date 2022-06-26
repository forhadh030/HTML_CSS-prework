# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    first_odds = 0
    for i in range(1, 100, 2):
        odd_numbers = i + first_odds
        print(odd_numbers)

first_odds()