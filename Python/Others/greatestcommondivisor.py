a = 200
b = 100

while b > 0:
    temp = a
    a = b
    b = temp % b

print(a)
