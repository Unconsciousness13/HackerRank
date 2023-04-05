n = int(input())
arr = [int(n) for n in input().split()]
arr = sorted(set(arr))
print(arr[-2])
