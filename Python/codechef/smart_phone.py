totalnums = int(input())
lst = []
for x in range(totalnums):
  lst.append(int(input()))
lst.sort()
revenue = 0
for x in range(len(lst)): 
  temprevenue = lst[x] * (len(lst) - (x))
  if revenue < temprevenue:
     revenue = temprevenue
print(revenue)
