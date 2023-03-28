def migratoryBirds(arr):
    max_count = -100
    max_id = -100

    for i in range(1, 6):
        if (arr.count(i) > max_count):
            max_count = arr.count(i)
            max_id = i
        elif (arr.count(i) == max_count and i < max_id):
            max_id = i

    return max_id


arr_count = int(input().strip())

arr = list(map(int, input().rstrip().split()))

result = migratoryBirds(arr)

print(str(result) + '\n')
