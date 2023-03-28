squares = [
    [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
    [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
    [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
    [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
    [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
    [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
    [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
    [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
]


def formingMagicSquare(s):
    costs = []
    for q in squares:
        cost = 0
        for i in range(3):
            for j in range(3):
                cost += abs(q[i][j]-s[i][j])
        costs.append(cost)
    return min(costs)


s = []

for _ in range(3):
    s.append(list(map(int, input().rstrip().split())))

result = formingMagicSquare(s)

print(str(result) + '\n')
