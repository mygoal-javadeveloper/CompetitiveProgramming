# Interview Question
# Write a program to do basic string compression.
# For a character which is consecutively repeated more than once,
# replace consecutive duplicate occurrences with the count of repetitions.
# For e.g. if a String has 'x' repeated 5 times, replace this "xxxxx" with "x5".
# Note : Consecutive count of every character in input string is less than equal to 9.
# Input Format : The first and the only line of input contains a string(no spaces in between).
# Output Format : Compressed string Constraints : 0 <= |S| <= 10^7
# Where |S| represents the length of string, S.
#
# Time Limit: 1sec
#
# Sample Input 1 :
# aaabbccdsa
# Sample Output 1 :
# a3b2c2dsa
# Sample Input 2 :
# aaabbcddeeeee
# Sample Output 2 : a3b2cd2e5

mystr = input().strip()
ans = ''
x = 0
while x < len(mystr):
  counter = 0
  tempstr = mystr[x].strip()
  ans = ans + tempstr
  counter += 1
  for y in range(x+1, len(mystr)):
    if mystr[y] == tempstr:
      counter += 1
      x += 1
    else:
      break
  x += 1
  if counter > 1:
    ans = ans + str(counter)

print(ans)