from collections import Counter


def migratoryBirds(arr):

    hmm = Counter(arr)

    maxvalue = max(hmm, key=hmm.get)
    return maxvalue


arr_count = int(input().strip())

arr = list(map(int, input().rstrip().split()))

result = migratoryBirds(arr)

print(str(result) + '\n')
