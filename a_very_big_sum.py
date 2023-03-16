def aVeryBigSum(ar):
    numb = 0
    for i in range(0, len(ar)):
        numb = numb + ar[i]
    return numb


ar_count = int(input().strip())

ar = list(map(int, input().rstrip().split()))

result = aVeryBigSum(ar)

print(str(result) + '\n')
