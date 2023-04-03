def freqQuery(queries):
    freq_count = {}
    output = []
    for q in queries:
        command = q[0]
        value = q[1]
        if command == 1:  # insert
            if value not in freq_count.keys():
                freq_count[value] = 1
            else:
                freq_count[value] += 1
        if command == 2:  # remove
            if value in freq_count.keys():
                if freq_count[value] > 0:
                    freq_count[value] -= 1
        if command == 3:  # check freq
            has_freq = 0
            if value in freq_count.values():
                has_freq = 1
            output.append(has_freq)

    return output


q = int(input().strip())

queries = []

for _ in range(q):
    queries.append(list(map(int, input().rstrip().split())))

ans = freqQuery(queries)

print('\n'.join(map(str, ans)))
print('\n')
