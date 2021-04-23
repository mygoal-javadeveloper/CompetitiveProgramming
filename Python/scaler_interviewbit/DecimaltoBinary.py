def findDigitsInBinary(A):
    binarystr = []
    if A == 0:
        return '0000'
    elif A > 0:
        while A > 0:
            binarystr.append(A % 2)
            A = A // 2
    binarystr.reverse()
    return ''.join(str(ele) for ele in binarystr)

print(findDigitsInBinary(10))
