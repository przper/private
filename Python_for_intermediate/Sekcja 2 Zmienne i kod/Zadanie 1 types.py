a = b = c = 10
print(a, b, c)
print(id(a), id(b), id(c))

a = 20
print(a, b, c)
print(id(a), id(b), id(c))

print("--------------------------")

a = b = c = [1, 2, 3]
print(a, b, c)
print(id(a), id(b), id(c))

a.append(4)
print(a, b, c)
print(id(a), id(b), id(c))

print("--------------------------")

x = 10
y = 10
print(id(x), id(y))

y = y + 1-1
print(id(y))

y = y +123456789-123456789
print(id(x), id(y))
