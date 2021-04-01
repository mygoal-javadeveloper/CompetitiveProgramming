for x in range(int(input().strip())):
    arr_size = int(input().strip())
    arr = list(map(int, input().strip().split()))
    index_add = 0
    arr.sort()
    while True:
        if arr[-1-index_add] - 1 in arr:
            arr.remove(arr[-1-index_add] - 1)
        if arr.index(arr[-1-index_add]) == 0:
            break
        index_add += 1
    print(sum(arr))


