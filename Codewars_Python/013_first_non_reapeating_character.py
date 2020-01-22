def first_non_repeating_letter(string):
    for l in string:
        num = string.count(l.upper())+string.count(l.lower()) if l.isalpha() else string.count(l)
        if num <=1:
            return l
    return ''

test =['','abba','aa','~><#~><',"Go hang a salami, I'm a lasagna hog!"]
print(first_non_repeating_letter('Agnieszka'))

for i in test:
    print(i.upper(),i.lower())
    print(first_non_repeating_letter(i))
    print(30*'-')
