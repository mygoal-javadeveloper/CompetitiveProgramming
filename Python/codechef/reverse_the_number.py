testcases = int(input())
while testcases > 0:
  num = int(input())
  length = len(str(num))
  reversenum = 0
  for x in range(length):
    reversenum = (reversenum * 10) + num % 10
    num = num // 10
  print(reversenum)
  testcases -= 1

