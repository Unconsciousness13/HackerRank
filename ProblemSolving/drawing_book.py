def pageCount(n, p):
    return min(int(p/2), int(n/2) - int(p/2))


n = int(input().strip())

p = int(input().strip())

result = pageCount(n, p)

print(str(result) + '\n')
