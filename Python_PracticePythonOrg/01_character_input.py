"""
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

    Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
    Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

"""
name = input("Please insert your name: ")
age = int(input("Please insert your age: "))
current_year = 2019
year = 2019+100-age

print("{}, you will be 100 years old in {}".format(name, year))

counter = int(input("Please input how many times do you want to display previous message: "))
print(counter*"{}, you will be 100 years old in {}\n".format(name, year))