"""
Write a program that asks the user how many Fibonnaci numbers
to generate and then generates them. Take this opportunity
to think about how you can use functions. Make sure to ask the user
to enter the number of numbers in the sequence to generate.

(Hint: The Fibonnaci seqence is a sequence of numbers where the next
number in the sequence is the sum of the previous two numbers in the sequence.
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""


def fibonacci(counter):
    seq = []
    for i in range(1, counter + 1):
        # print(i)
        if i < 3:
            seq.append(1)
            # print("Iteration {} - Sequence {}".format(i, seq)) #debug
        else:
            # print(seq[i-3]) #debug
            # print(seq[i-2]) #debug
            seq.append((seq[i - 3] + seq[i - 2]))
            # print("Iteration {} - Sequence {}".format(i, seq)) #debug
    return seq


counter = int(input("How long Fibonacci sequence to generate?: "))
print("Fibonacci sequence of lenght {}: {}".format(counter, fibonacci(counter)))
