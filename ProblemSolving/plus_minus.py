def plusMinus(arr):
    negative = 0
    zeros = 0
    positive = 0

    for num in arr:
        if num < 0:
            negative += 1
        elif num > 0:
            positive += 1
        else:
            zeros += 1
    positive_percents = float(100 * positive / n / 100)
    negative_percents = float(100 * negative / n / 100)
    zeros_percents = float(100 * zeros / n / 100)
    print(positive_percents)
    print(negative_percents)
    print(zeros_percents)


n = int(input().strip())

arr = list(map(int, input().rstrip().split()))

print(plusMinus(arr))
