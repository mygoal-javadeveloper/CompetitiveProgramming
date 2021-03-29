# cook your dish here
for testcases in range(int(input().strip())):
  for numberofgames in range(int(input().strip())):
    initial_stage, number_coinsnrounds, end_results = list(map(int, input().strip().split()))
    if initial_stage == end_results or not(number_coinsnrounds % 2):
      print(number_coinsnrounds >> 1)
      continue
    print((number_coinsnrounds >> 1) + 1)
