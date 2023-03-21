def rotLeft(a, d):
    res = a.copy()
    for i in range(d):
        rot1 = res[0]
        res.remove(rot1)
        res.append(rot1)

    return res


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

d = int(first_multiple_input[1])

a = list(map(int, input().rstrip().split()))

result = rotLeft(a, d)

print(' '.join(map(str, result)))
print('\n')
