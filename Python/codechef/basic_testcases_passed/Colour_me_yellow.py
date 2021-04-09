# You need to color a floor plan which is of size 3 x n. (3 rows and n columns)
#
# You have tiles of size 1x1 of different colors, specifically you have:
#
# r tiles of color red
#
# g tiles of color green
#
# b tiles of color blue
#
# What is the maximum number of columns you can color such that every column has at least 1 red and 1 blue?
#
# Input
# First line contains a single integer T, the number of testcases
#
# Each testcase contains a single line containing four space separated integers, namely n, r, g, b.
#
# Output
# For each testcase output a new line containing a single integer, the answer to the problem
#
# Constraints
# 1≤T≤105
# 0≤r,g,b≤109
# 0≤n≤3.109
# Sample Input
# 3
# 4 3 3 4
# 4 4 1 4
# 2 4 1 4
# Sample Output
# 3
# 3
# 2

for testcases in range(int(input().strip())):
    rows = 3
    cols, red, green, blue = list(map(int, input().strip().split()))
    while (cols > min(red, blue)) or ((rows*cols) > (red+green+blue)):
        cols -= 1
    print(cols)
