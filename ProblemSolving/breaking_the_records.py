def breakingRecords(scores):
    minimum_count = 0
    maximum_count = 0
    minimum = scores[0]
    maximum = scores[0]

    for index in range(len(scores)):
        score = scores[index]
        if score < minimum:
            minimum = score
            minimum_count += 1
        if score > maximum:
            maximum = score
            maximum_count += 1

    return(maximum_count, minimum_count)


n = int(input().strip())

scores = list(map(int, input().rstrip().split()))

result = breakingRecords(scores)

print(' '.join(map(str, result)))
print('\n')
