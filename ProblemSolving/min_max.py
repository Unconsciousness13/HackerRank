def miniMaxSum(arr):
    minimum = 0
    maximum = 0
    maxnum = max(arr)
    minnum = min(arr)
    maxList = arr.copy()
    minList = arr.copy()
    maxList.remove(minnum)
    minList.remove(maxnum)
    minimum = sum(minList)
    maximum = sum(maxList)

    return (print(minimum, maximum))


arr = list(map(int, input().rstrip().split()))

miniMaxSum(arr)
