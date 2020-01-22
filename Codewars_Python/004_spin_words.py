def spin_words(sentence):
    str=[]
    for s in sentence.split():
        if len(s)>4:
            str.append(s[::-1])
        else:
            str.append(s)
    return ' '.join(str)

words ="Agnieszka jest bardzo ladna"
print(spin_words(words))
