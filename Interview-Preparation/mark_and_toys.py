def maximumToys(prices, k):
    prices.sort()
    toys = 0
    suma = 0
    for i in prices:
        if (i <= k and suma+i <= k):
            suma += i
            toys += 1
    return toys


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

k = int(first_multiple_input[1])

prices = list(map(int, input().rstrip().split()))

result = maximumToys(prices, k)

print(str(result) + '\n')
