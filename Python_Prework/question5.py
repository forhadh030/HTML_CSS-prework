# Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

from operator import truediv


def is_consecutive(a_list):
    for i in range(my_list):
        if i == i[1:]:
            return True
        else:
            return False

my_list = [2, 2, 3, 4, 5, 6]
print(is_consecutive(my_list))