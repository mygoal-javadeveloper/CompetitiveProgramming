for x in range(int(input().strip())):
  num_cols = len(list(map(int, input().strip().split())))
  temp = 1
  max = 0
  lst = []
  for y in range(num_cols):
    templst = ['C'+ str(temp), sum(list(map(int, input().strip().split())))]
    if max < templst[1]:
      max = templst[1]
    lst.append(templst)
    temp += 1
  for z in lst:
    if z[1] == max:
      print(z[0])
      break
