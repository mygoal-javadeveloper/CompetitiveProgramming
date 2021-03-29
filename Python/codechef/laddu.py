# cook your dish here
for testcases in range(int(input().strip())):
  num_activites, origin = list(input().strip().split())
  laddus = 0
  for x in range(int(num_activites)):
    activity = list(input().strip().split())
    if activity[0].upper() == 'CONTEST_WON':
      bonus = 0
      if int(activity[1]) <= 20:
        bonus = 20 - int(activity[1])
      laddus += (300 + bonus)
    elif activity[0].upper() == 'TOP_CONTRIBUTOR':
      laddus += 300
    elif activity[0].upper() == 'BUG_FOUND':
      laddus += int(activity[1])
    elif activity[0].upper() == 'CONTEST_HOSTED':
      laddus += 50
  if origin.upper() == 'INDIAN':
    print(laddus // 200)
  elif origin.upper() == 'NON_INDIAN':
    print(laddus // 400)

