def birthday(s, d, m):
    total = 0
    birthday_el = d
    birthday_month = m
    num_square_arr = s
    sum_to_compare = 0
    for index in range(n-birthday_month+1):
        sum_to_compare = sum(num_square_arr[index:index + birthday_month])
        if sum_to_compare == birthday_el:
            total += 1
        index += 1
    return total


n = int(input().strip())

s = list(map(int, input().rstrip().split()))

first_multiple_input = input().rstrip().split()

d = int(first_multiple_input[0])

m = int(first_multiple_input[1])

result = birthday(s, d, m)

print(str(result) + '\n')
