def divisibleSumPairs(n, k, ar):
    counter = 0
    current = 0
    while True:
        if current == n-1:
            break
        for i in range(1, n+1):
            if i > current:
                if (ar[current] + ar[i]) % k == 0:
                    counter += 1
            if i == n-1:
                current += 1
                break
    return counter


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

k = int(first_multiple_input[1])

ar = list(map(int, input().rstrip().split()))

result = divisibleSumPairs(n, k, ar)

print(str(result) + '\n')
