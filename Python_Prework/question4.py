# Write a function to return if the given year is a leap year. A leap year is divisible by 4
# but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    leap = a_year % 4
    if leap == 0:
        return True
    else:
        return False
year = int(input("Do you want to know if it's leap year? What year are we in? Enter the 4 digit: "))
print(is_leap_year(year))