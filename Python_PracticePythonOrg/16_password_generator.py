"""
Write a password generator in Python. Be creative with how you generate
passwords - strong passwords have a mix of lowercase letters, uppercase
letters, numbers, and symbols. The passwords should be random,
generating a new password every time the user asks for a new password.
Include your run-time code in a main method.

Extra:
    Ask the user how strong they want their password to be.
    For weak passwords, pick a word or two from a list.
"""
import random


def gen1(chars, length):
    password = ""
    for number in range(length):
        password += random.choice(chars)
    return password


def gen2(length):
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    special_signs = "!@#$%^&*()?"
    password = []
    password.append(random.choice(lowercase))
    password.append(random.choice(uppercase))
    password.append(random.choice(numbers))
    password.append(random.choice(special_signs))
    for number in range(length - 4):
        password.append(random.choice("".join([lowercase, uppercase, numbers, special_signs])))
    # print(password)
    random.shuffle(password)
    # print(password)
    return "".join(password)


lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special_signs = "!@#$%^&*()?"

chars = "".join([lowercase, uppercase, numbers, special_signs])
# print(chars)

# password_length = int(input("How long do you want your password?: "))
password_length = 10

print("Generator 1:")
for number in range(6):
    print("Generated password:", gen1(chars, password_length))

print()
print()

print("Generator 2 (by topor):")
for number in range(6):
    print("Generated password:", gen2(password_length))

# print(gen2(password_length))
