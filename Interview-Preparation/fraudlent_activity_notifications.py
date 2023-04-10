import bisect


def activityNotifications(expenditure, d):
    if len(expenditure) <= d:
        return 0
    count = 0
    trail_sort = sorted(expenditure[:d])
    for i in range(d, len(expenditure)):
        exp = expenditure[i]
        if exp >= 2*sum(trail_sort[~(d//2):d//2+1])/(2-d % 2):
            count += 1
        trail_sort.pop(bisect.bisect_left(trail_sort, expenditure[i-d]))
        bisect.insort_right(trail_sort, exp)

    return count


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

d = int(first_multiple_input[1])

expenditure = list(map(int, input().rstrip().split()))

result = activityNotifications(expenditure, d)

print(str(result) + '\n')
