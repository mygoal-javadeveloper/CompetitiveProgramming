# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

lst = [10, 15, 3, 7]
k = 17

def findtwonumbers(lst , k):
    lst.sort()
    for x in range(len(lst)-1, 0, -1):
        temp = abs(lst[x] - k)
        if temp in lst:
            return True
    else:
        return False
print(findtwonumbers(lst , k))