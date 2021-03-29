testcases = int(input())
for x in range(testcases):
  input_str = input()
  firsthalf_str = input_str[:len(input_str)//2]
  secondhalf_str = input_str[(len(input_str)//2) + (len(input_str)%2):]
  tempbool = True
  for y in range(len(firsthalf_str)):
    if firsthalf_str.count(firsthalf_str[y]) == secondhalf_str.count(firsthalf_str[y]):
      continue
    else:
      tempbool = False
      break
  if tempbool:
    print('YES')
  else:
    print('NO')