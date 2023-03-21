def hourglassSum(arr):


arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

result = hourglassSum(arr)

print(str(result) + '\n')
