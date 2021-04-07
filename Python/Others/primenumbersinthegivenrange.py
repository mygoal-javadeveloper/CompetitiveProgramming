y = 100
primenumberlst = [i for i in range(y+1) if all(i%j for j in range(2, i)) and i != 0 and i != 1]
print(primenumberlst)
