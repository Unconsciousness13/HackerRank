def kangaroo(x1, v1, x2, v2):
    initial1 = x1
    step1 = v1
    initial2 = x2
    step2 = v2
    secondl = []
    jump1 = 0
    jump2 = 0

    for i in range(10000):
        initial1 += step1
        initial2 += step2
        jump1 += 1
        jump2 += 1

        secondl.append((initial2, jump2))

        if (initial1, jump1) in secondl:
            return "YES"

    else:
        return "NO"


first_multiple_input = input().rstrip().split()

x1 = int(first_multiple_input[0])

v1 = int(first_multiple_input[1])

x2 = int(first_multiple_input[2])

v2 = int(first_multiple_input[3])

result = kangaroo(x1, v1, x2, v2)

print(result + '\n')
