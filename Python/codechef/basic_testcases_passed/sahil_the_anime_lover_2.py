# Codechef
#
# Sahil is the greatest anime lover of all time.
# He loves to watch anime at any time of the day.
# He has unlimited collections of anime.
# Suppose N is total number of anime episodes watched by him.
# Anime Factor is given by Z=Sum of all the prime numbers
# which are less than equal to N.
# Help him find the anime factor.
#
# Input
# First line contains no of test cases.
# Each line of test case contains an integer N.
# Output
# Print Anime factor 'Z' for each test case on a new line.
# Constraints:
# 1 <= N <= 6(10 points)
# 1 <= N <= 10^4(40 points)
# 1 <= N <= 10^7(50 points)
# Example
# Input:
# 2
# 1
# 2
#
# Output:
# 0
# 2

for testcases in range(int(input().strip())):
    num = int(input().strip()) + 1
    primenumberlst = [True] * num
    primenumberlst[0] = False
    primenumberlst[1] = False
    for y in range(2, num):
        if primenumberlst[y] == False:
            continue
        else:
            for z in range(2, num//2):
                product = y * z
                if product < num:
                    primenumberlst[product] = False
                else:
                    continue
    primenumber_sum = 0
    for i in range(num):
        if primenumberlst[i]:
            primenumber_sum += i
    print(primenumber_sum)

