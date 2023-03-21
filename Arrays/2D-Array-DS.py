def hourglassSum(arr):
    best = -90
    for row in range(4):
        for col in range(4):
            sum1 = arr[row][col] + arr[row][col+1] + arr[row][col+2]
            sum2 = arr[row+1][col+1]
            sum3 = arr[row+2][col] + arr[row+2][col+1] + arr[row+2][col+2]
            total = sum1 + sum2 + sum3
            if total >= best:
                best = total
    return best


arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

result = hourglassSum(arr)

print(str(result) + '\n')
