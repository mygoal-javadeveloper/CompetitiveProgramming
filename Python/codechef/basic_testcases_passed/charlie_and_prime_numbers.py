# Charlie has a fascination for Prime Numbers.But he never went to school
# so he always makes a mistake when he is asked to tell whether a number
# is a Prime Number or not.So, he asks his brother Alan to help him out with this.
# Your job is to help Alan in writing a program which prints
# THE SUM of all prime numbers between M and N (inclusive).
#
# Input
# The first Line of Input will contain an Integer T ,
# Denoting the number of Test Cases.
# The next T Lines, each, will have 2 space separated Integers M and N
# Output
# For Each Test Case, Output a single Line containing the SUM of all Prime Numbers
# between M and N (inclusive).It would be advisable to use Long Datatype for storing the sum.
# Constraints
# Subtask 1: (30 Points): M <=10^3, N<=10^3
# Subtask 2: (70 Points): M<=5*10^6, N<=5*10^6
# Example
# Input:
# 2
# 1 8
# 37 45
#
# Output:
# 17
# 121
#
# Explanation
# In the first case, Prime Numbers between 1 and 8 are 2, 3, 5 and 7.
# Their sum is 17.
# In the second case, Prime Numbers between 37 and 45 are 37, 41 and 43.
# Their sum is 121.

for testcases in range(int(input().strip())):
    startnum, endnum = list(map(int, input().strip().split()))
    primenumlst = [i for i in range(startnum, endnum+1) if all(i%j for j in range(2, i//2 +1)) and i != 0 and i != 1]
    print(sum(primenumlst))