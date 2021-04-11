# Geek wants to sell his house.
# There are N buyers in the market and ith buyer will buy the house
# on the jth day at j*A[i]+B[i] rupees.
# You are given Q queries.
# Each query contains an integer K, for each query,
# you have to calculate the maximum cost of the house at which Geek can sell on the Kth day.
#
# Example 1:
#
# Input:
# N = 2, Q = 2
# A[] = {1, 3}
# B[] = {4, 1}
# Queries[] = {1, 2}
# Output:
# 5 7
# Explanation:
# 1st query:
# 1st Buyer can buy at cost = 1 * 1 + 4 = 5
# 2nd Buyer can buy at cost = 1 * 3 + 1 = 4
# Maximum cost = max(5, 4) = 5
# 2nd query:
# 1st Buyer can buy at cost = 2 * 1 + 4 = 6
# 2nd Buyer can buy at cost = 2 * 3 + 1 = 7
# Maximum cost = max(6, 7) = 7
# Example 2:
#
# Input:
# N = 1, Q = 1
# A[] = {1}
# B[] = {1}
# Queries[] = {2}
# Output:
# 3
# Your Task:
# You don't need to read input or print anything. Your task is to complete the function solve( ) which takes integer N, array A[ ], array B[ ], integer Q and array Queries[ ] as input parameters and returns the array consisting of answer to each query.
#
# Expected Time Complexity: O((N + Q) * LogN)
# Expected Auxiliary Space: O(N + max(Queries[i]))
#
# Constraints :
# 1 ≤ N, Q ≤ 105
# 1 ≤ A[i], B[i] ≤ 106
# 1 ≤ Queries[i] ≤ min(10*N, 105)


def solve(N, A, B, Q, Queries):
    # code here
    maxprice = []
    for day in Queries:
        templst = []
        for x in range(N):
            templst.append(day*A[x]+B[x])
        maxprice.append(max(templst))
    return maxprice



print(solve(2, [1, 3], [4, 1], 2, [1, 2]))

# print(solve(1, [1], [1], 1, [2]))