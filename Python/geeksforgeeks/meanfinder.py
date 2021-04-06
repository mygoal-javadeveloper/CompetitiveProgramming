# You are given a mean M, and an integer D.
# The mean M is the mean of 3 numbers A, B, and C. Find the mean of A, B, C, and D.
#
# Example:
#
# Input:
# D = 5
# M = 1
# Output:
# 2
# Explanation:
# Mean of 3 numbers is 1. If we include 5 and find the new mean, it will be 2.
# Your Task:
# This is a function problem. You do not need to take any input.
# Complete the function mean() and return the new mean.
#
# Constraints:
# 1 <= D, M <= 108



D = 5
M = 1

def findmean(D, M):
    return (((3 * M) + D) / 4)


print(findmean(D, M))

