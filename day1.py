"""
Write a Python function that calculates the sum of a list of numbers:

The function should accept a list of numbers and return the sum of those numbers.
If no argument is provided (that is, numbers is None), return the sum of the numbers 1 to 100 
(Note that this is not the same as an empty list of numbers being passed in. In that case the sum returned will be 0).
"""

def calculate_sum(numbers=None):
    if numbers is None:
        return sum(range(1,101))
    else:
        return sum(numbers)
    

numbers = [1,2,3,4,5]
print(calculate_sum(numbers))