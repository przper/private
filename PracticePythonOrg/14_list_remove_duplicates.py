"""
Write a program (function!) that takes a list and returns a new list that contains
all the elements of the first list minus all the duplicates.

Extras:
    - Write two different functions to do this - one using a loop
      and constructing a list, and another using sets.
    - Go back and do Exercise 5 using sets, and write the solution
      for that in a different function.

"""


def list_cleaner(list_with_duplicates):
    new_list = []
    for item in list_with_duplicates:
        if item not in new_list:
            new_list.append(item)
    return new_list


"""
def list_cleaner_with_set(list_with_duplicates):
    new_list = set()
    for item in list_with_duplicates:
        new_list.add(item)
    return new_list
"""


# cleaner version:
def list_cleaner_with_set(list_with_duplicates):
    return list(set(list_with_duplicates))


a = [1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 9, 9, 10]

print("Base list:", a)
print("List without duplicates:", list_cleaner(a))
print("List without duplicates:", list_cleaner_with_set(a))
