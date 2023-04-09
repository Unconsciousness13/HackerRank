def countSwaps(a):
    swaps = 0
    for i in range(len(a)-1):
        for j in range(0, len(a)-i-1):
            if(a[j] > a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]
                swaps += 1

    print(f"Array is sorted in {swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")


n = int(input().strip())

a = list(map(int, input().rstrip().split()))

countSwaps(a)
