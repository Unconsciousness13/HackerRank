def split_and_join(line):
    res = ''
    for l in line:
        if l == ' ':
            l = '-'
        res += l
    return res
    # short code return "-".join(line.split(" "))


line = input()
print(split_and_join(line))
