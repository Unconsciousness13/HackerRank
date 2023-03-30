def twoStrings(s1, s2):
    res = "NO"
    for l in s1:
        if l in s2:
            res = "YES"
            break
    return res


q = int(input().strip())

for q_itr in range(q):
    s1 = input()

    s2 = input()

    result = twoStrings(s1, s2)

    print(result + '\n')
