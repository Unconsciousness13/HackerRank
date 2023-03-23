def getTotalX(a, b):
    total = 0
    for i in range(1, 100 + 1):
        if all(i % x == 0 for x in a) and all(x % i == 0 for x in b):
            total += 1
    return total


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

arr = list(map(int, input().rstrip().split()))

brr = list(map(int, input().rstrip().split()))

total = getTotalX(arr, brr)

print(str(total) + '\n')
