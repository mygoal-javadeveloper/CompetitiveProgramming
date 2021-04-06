# You are given a two-digit number N. Find the sum of its digits
#
# Example:
#
# Input:
# N = 25
# Output:
# 7
# Your Task:
# This is a function problem. You do not need to take any input.
# just Complete the function digitsSum() and return the sum of digits of N.
#
# Constraints:
# 10 <= N <= 99

N = 25
n_sum = 0
while N > 0:
    n_sum += N % 10
    N = N // 10
print(n_sum)