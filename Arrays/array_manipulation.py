def arrayManipulation(n, queries):
    acc = {}
    for [a, b, k] in queries:
        acc[a] = (acc[a] if a in acc else 0) + k
        acc[b+1] = (acc[b+1] if b+1 in acc else 0) - k

    last = 0
    m = 0
    for i in range(1, n+1):
        curr = acc[i] if i in acc else 0
        last = last + curr
        if (last > m):
            m = last

    return m


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

queries = []

for _ in range(m):
    queries.append(list(map(int, input().rstrip().split())))

result = arrayManipulation(n, queries)

print(str(result) + '\n')
