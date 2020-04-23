"""
Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user.
Hint: how does an even / odd number react differently when divided by 2?

Extras:

    - If the number is a multiple of 4, print out a different message.
    - Ask the user for two numbers: one number to check (call it num) and
    one number to divide by (check). If check divides evenly into num,
    tell that to the user. If not, print a different appropriate message.

"""

number = int(input("Please insert a number: "))
if number % 4 == 0:
    print("The number you inserted is dividible by 4")
elif number % 2 == 0:
    print("The number you inserted is even number")
else:
    print("The number you inserted is odd number")

num = int(input("Please insert a number: "))
check = int(input("Please insert another number: "))

if num % check == 0:
    print("The numbers are dividible by each other")
else:
    print("The numbers aren't dividible by each other")