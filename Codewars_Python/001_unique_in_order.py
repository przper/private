def unique_in_order(iterable):
    if len(iterable)==0:
        lst=iterable
    else:
        lst=[iterable[0]]
        for i in iterable:
            if i != lst[-1]:
                lst.append(i)
    return lst
    
unique_in_order('AAAABBBCCDAABBB')
unique_in_order('ABBCcAD')
unique_in_order([1,2,2,3,3])

print('TADA:',unique_in_order(''))
print('TADA:',unique_in_order([]))
print('TADA:',unique_in_order('AAAABBBCCDAABBB'))
print('TADA:',unique_in_order('ABBCcAD'))
print('TADA:',unique_in_order([1,2,2,3,3]))
