"""
Create a program that asks the user for a number and then prints out
a list of all the divisors of that number. (If you don’t know what a divisor is,
it is a number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
"""

number = int(input("Please enter a number: "))
for i in range(1, number+1):
    print(i) if number % i == 0 else 0

#no z tego jestem dumny