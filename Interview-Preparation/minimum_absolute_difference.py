def minimumAbsoluteDifference(arr):
    arr = sorted(arr)
    res = abs(arr[0] - arr[1])
    for i in range(len(arr)-1):
        if res > abs(arr[i]-arr[i+1]):
            res = abs(arr[i]-arr[i+1])

    return res


n = int(input().strip())

arr = list(map(int, input().rstrip().split()))

result = minimumAbsoluteDifference(arr)

print(str(result) + '\n')
