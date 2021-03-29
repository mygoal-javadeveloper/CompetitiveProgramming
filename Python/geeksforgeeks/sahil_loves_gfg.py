for x in range(int(input().strip())):
  input_str = input().strip()
  # if 'gfg' in input_str:
  #   print(input_str.count('gfg'))
  # else:
  #   print(-1)
  # above code giving wrong answer in 'fgrgfgfgdg'
  gfg_count = 0
  for y in range(len(input_str)-2):
      if input_str[y:y+3] == 'gfg':
          gfg_count += 1
  if gfg_count:
      print(gfg_count)
  else:
      print(-1)



