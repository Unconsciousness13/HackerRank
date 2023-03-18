def compareTriplets(a, b):
    a_points = 0
    b_points = 0
    for i in range(len(a)):
        if a[i] < b[i]:
            b_points += 1
        elif a[i] > b[i]:
            a_points += 1
    return (a_points, b_points)


a = list(map(int, input().rstrip().split()))

b = list(map(int, input().rstrip().split()))

result = compareTriplets(a, b)

print(' '.join(map(str, result)))
print('\n')
# pass
