import math

def isPrime(A):
    if A <= 1:
        return 0
    else:
        for x in range(2, int(math.sqrt(A)) + 1):
            if not A % x:
                return 0
        return 1



A = 13
print(isPrime(A))
# output: 1

A = 21
print(isPrime(A))
# output: 0