testcases = int(input().strip())
for x in range(testcases):
  numberofcars = int(input().strip())
  lst = list(map(int, input().strip().split()))
  count = 1
  for y in range(1, len(lst)):
      if lst[y] > lst[y-1]:
          lst[y] = lst[y-1]
      elif lst[y] <= lst[y-1]:
          count += 1
  print(count)