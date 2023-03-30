def countTriplets(arr, r):
    possible = {}
    combo = {}
    res = 0
    for el in arr:
        secondEl = el * r
        if(el in combo):
            res += combo[el]
        if(el in possible):
            combo[secondEl] = combo.get(secondEl, 0)+possible.get(el)
        possible[secondEl] = possible.get(secondEl, 0)+1
    print(combo)
    print(possible)
    return res


nr = input().rstrip().split()

n = int(nr[0])

r = int(nr[1])

arr = list(map(int, input().rstrip().split()))

ans = countTriplets(arr, r)

print(str(ans) + '\n')
