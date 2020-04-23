def camel_case(string):
    lst=string.split(' ')
    new_lst=[]
    for item in lst:
        new_lst.append(item.capitalize())
    return "".join(new_lst)

print(camel_case("hello case"))
print(camel_case("camel case word"))
