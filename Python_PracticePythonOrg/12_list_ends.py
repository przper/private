"""
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
and makes a new list of only the first and last elements of the given list.
For practice, write this code inside a function.
"""

import random


def list_gutter(list):
    return [list[0], list.pop()]


a = list(random.sample(range(30), 5 + random.randrange(5)))
a.sort()
print("List 'a':", a, "List lenght:", len(a), '\n')

b = list_gutter(a.copy())
print("Gutted list:", b)
