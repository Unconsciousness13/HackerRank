
def countInversions(a):
    count = 0

    def merge(a):
        nonlocal count
        if len(a) < 2:
            return a
        L = merge(a[:len(a) // 2])
        R = merge(a[len(a) // 2:])
        n = m = 0
        C = []
        while n < len(L) and m < len(R):
            if L[n] <= R[m]:
                C.append(L[n])
                n += 1
            else:
                C.append(R[m])
                m += 1
                count += len(L) - n
        return C + L[n:] + R[m:]
    merge(a)
    return count


t = int(input().strip())

for t_itr in range(t):
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countInversions(arr)

    print(str(result) + '\n')
