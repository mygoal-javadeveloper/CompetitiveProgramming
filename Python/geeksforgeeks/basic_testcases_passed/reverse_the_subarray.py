# Given an array A[ ] of N elements and Q queries .
# Each query is of two types:
#
# If the type of query is 1 then it consists of two integers L and R.
# Your task is to reverse the subarray of A from index L to R (both inclusive).
# If the type of query is 2 then it consists of one integer X.
# Your task is to find the element at index X.
# Note: 1-based indexing is used.
#
# Example 1:
#
# Input:
# N = 5, Q = 3
# A[] = {4, 3, 1, 2, 6},
# Queries = {{2, 1},
#            {1, 1, 4},
#            {2, 2}}
# Output:
# 4 1
# Explanation:
# A[] = {4, 3, 1, 2, 6}
# For the 1st query, ans = A[X] = 4
# After the 2nd query, A[] = {2, 1, 3, 4, 6}
# For the 3rd query, ans = A[X] = 1
# Example 2:
#
# Input:
# N = 2, Q = 2
# A[] = {1, 2}
# Queries = {{1, 1, 1},
#            {2, 1}}
# Output:
# 1
# Explanation:
# A[] = {1, 2}
# After the 1st query, A[] = {1, 2}
# For the 2nd query, ans = A[X] = 1
# Your Task:
# Your task is to complete the function solveQueries( )
# which takes the integer N, array A[ ], integer Q and 2D array Queries[ ][ ]
# as input parameters and returns a list containing the answer of
# queries of type 2 in the order they appear.
#
# Constraints:
# 1 ≤ N, Q ≤ 105
# 1 ≤ A[i] ≤ 109
# If Queries[i][0] = 1, 1 ≤ Queries[i][1] ≤ Queries[i][2] ≤  N
# If Queries[i][0] = 2, 1 ≤ Queries[i][1] ≤ N


def solveQueries(N, A, Q, Queries):
    anslst = []
    for q in Queries:
        if q[0] == 2:
            anslst.append(A[q[1]-1])
        if q[0] == 1:
            if q[1] != q[2]:
                templst = A[q[2]-1:q[1]:-1]
                ret = []
                for x in range(len(templst)):
                    ret.append(templst[x])
                del templst
                A[q[1]-1:q[2]] = ret

    return anslst

N = 5
Q = 3
A = [4, 3, 1, 2, 6]
Queries = [[2, 1],
           [1, 1, 4],
           [2, 2]]

# N = 2
# Q = 2
# A = [1, 2]
# Queries = [[1, 1, 1],
#            [2, 1]]

print(solveQueries(N, A, Q, Queries))