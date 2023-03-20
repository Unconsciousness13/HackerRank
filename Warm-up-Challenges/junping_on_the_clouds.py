def jumpingOnClouds(c):
    i = 0
    jumps = -1
    while i < len(c):
        jumps += 1
        if (i < len(c)-2) and (c[i+2] == 0):
            i += 1
        i += 1
    return jumps


n = int(input().strip())

c = list(map(int, input().rstrip().split()))

result = jumpingOnClouds(c)

print(str(result) + '\n')
