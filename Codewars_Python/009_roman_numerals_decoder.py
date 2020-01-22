def solution(roman):
    print(roman,id(roman))
    number=0
    dict={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
    dict1={'CM':900,'CD':400,'XC':90,'XL':40,'IX':9,'IV':4}
    for num in list(dict1.keys()):
        if num in roman:      
            number+=dict1.get(num)
    my_roman=roman
    print(my_roman,id(my_roman))
    for i in list(dict1.keys()):
        my_roman=my_roman.replace(i,'')
    print(my_roman,id(my_roman))
    for s in my_roman:
        number+=dict.get(s)
        print(s,dict.get(s),number)
    return number

print(solution('MMCDLIV'))
print(solution('MCXLIV'))
