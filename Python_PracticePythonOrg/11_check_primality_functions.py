"""
Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.).
You can (and should!) use your answer to Exercise 4 to help you.
Take this opportunity to practice using functions, described below.
"""


def get_dividers(number):
    return [i for i in range(1, number + 1) if number % i == 0]


number = int(input("Please enter a number: "))

dividers = get_dividers(number)
# print(dividers) #debug
if len(dividers) > 2:
    print("The number {} is not a prime number".format(number))
else:
    print("The number {} is a prime number".format(number))