"""
Write a program (using functions!) that asks the user for a long string
containing multiple words. Print back to the user the same string,
except with the words in backwards order. For example, say I type the string:
  My name is Michele

Then I would see the string:
  Michele is name My

shown back to me.
"""


def inverter(string):
    split_string = string.split(' ')
    reverse_string = []
    for i in range(len(split_string)):
        reverse_string.append(split_string.pop())
    return " ".join(reverse_string)


def reverse_word(w):
    return ' '.join(w.split()[::-1])


my_string = "my wife has a nice ass"
inverter(my_string)
print("Reversed string:", inverter(my_string))
print("Reversed string:", reverse_word(my_string))
