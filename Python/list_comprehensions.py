x = int(input())
y = int(input())
z = int(input())
n = int(input())

mtr = []

for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if sum([i+j+k]) != n:
                mtr.append([i, j, k])

print(mtr)
