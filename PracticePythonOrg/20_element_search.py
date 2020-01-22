"""
Write a function that takes an ordered list of numbers
(a list where the elements are in order from smallest to largest)
and another number. The function decides whether or not the given
number is inside the list and returns (then prints) an appropriate boolean.

Extras:
    - Use binary search.
"""
import random

def boolean_search(random_list, number):
    half = sum(random_list)/2
    boolean_list = []
    for n in random_list:
        if n <



a = list(random.sample(range(30), 10 + random.randrange(4)))
a.sort()
print("List a:", a, "Length:", len(a))
