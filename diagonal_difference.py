def diagonalDifference(arr):
    d1 = 0
    d2 = 0

    for i in range(len(arr)):
        for j in range(len(arr)):
            # finding sum of primary diagonal
            if i == j:
                d1 += arr[i][j]
            # finding sum of secondary diagonal
            if i == n - j - 1:
                d2 += arr[i][j]

    # Absolute difference of the sums
    # across the diagonals
    return abs(d1 - d2)


n = int(input().strip())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(arr)

print(str(result) + '\n')
