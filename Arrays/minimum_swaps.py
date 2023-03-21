def minimumSwaps(arr):
    swaps = 0
    tmp = {}

    for i, val in enumerate(arr):
        tmp[val] = i

    for i in range(len(arr)):
        # because they are consecutives, I can see if the number is where it belongs
        if arr[i] != i+1:
            swaps += 1
            t = arr[i]
            arr[i] = i+1
            arr[tmp[i+1]] = t

            # Switch also the tmp array, no need to change i+1 as it's already good now
            tmp[t] = tmp[i+1]

    return swaps


n = int(input())

arr = list(map(int, input().rstrip().split()))

res = minimumSwaps(arr)

print(str(res) + '\n')
