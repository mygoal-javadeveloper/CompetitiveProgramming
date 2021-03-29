testcases = int(input())
for x in range(testcases):
  num = int(input())
  primefactorisation_numfactor = 0
  fivesmatters = 5  # 2s and 5s in prime factorisation of n! matter.
  while num // fivesmatters:
     primefactorisation_numfactor += num // fivesmatters
     fivesmatters *= 5
  print(primefactorisation_numfactor)