# learnt this code on codeX, interviewbit, scaler
from math import sqrt
from functools import reduce

num = 126
factorslst = sorted(set(reduce(list.__add__, ([i, num//i] for i in range(1, int(sqrt(num)+1), (1 if not num % 2 else 2)) if not num % i))))

print(factorslst)