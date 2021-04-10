#GeeksForGeeks
# Given two positive integers M and N, after adding M and N
# if number of digits in M+N and N are same return N otherwise return M+N.
#
# Input:
# First line of input contains T denoting number of testcases.
# For each test case there will be two space seperated positive integers M and N.
#
# Output:
# If number of digits in M+N is same as N print N otherwise print M+N.
#
# Constraints:
# 1 <= T <= 100
# 1 <= M <= 109
# 1 <= N <=109
#
# Example:
# Input:
# 2
# 44 22
# 99 12
#
# Output:
# 22
# 111

from math import *
for testcases in range(int(input().strip())):
    m, n = list(map(int, input().strip().split()))
    sum_of_input = m+n
    number_of_sum_digits = int(log10(sum_of_input) + 1)
    number_of_n_digits = int(log10(n) + 1)
    if number_of_sum_digits == number_of_n_digits:
        print(n)
    else:
        print(sum_of_input)
