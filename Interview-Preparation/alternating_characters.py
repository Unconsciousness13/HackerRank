def alternatingCharacters(s):
    res = 0
    for i in range(len(s)):
        if len(s) == 1:
            break
        if s[0] == s[1]:
            res += 1
            s = s[1:]
        else:
            s = s[1:]
    return res


q = int(input().strip())

for q_itr in range(q):
    s = input()

    result = alternatingCharacters(s)

print(str(result) + '\n')
