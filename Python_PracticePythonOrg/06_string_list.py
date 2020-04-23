"""
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
"""

string = input("Please enter a word: \n")
#print(string[:])
#print(string[::-1])


if string[0:]==string[::-1]:
    print("Your word is palindrome")
else:
    print("Your word isn't palindrome")