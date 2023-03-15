def sockMerchant(n, ar):
    ar.sort(reverse=False)
    pairs = 0
    cur = 0
    proper = cur + 1
    while True:
        if proper > len(ar):
            break
        if len(ar) > 1 and ar[0] == ar[1]:
            pairs += 1
            ar.remove(ar[0])
            ar.remove(ar[0])
        else:
            proper += 1
        if proper == len(ar):
            ar.remove(ar[0])
            proper = 1
    return pairs


n = int(input().strip())

ar = list(map(int, input().rstrip().split()))

result = sockMerchant(n, ar)

print(str(result) + '\n')
