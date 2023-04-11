from collections import Counter


def makeAnagram(a, b):
    a = Counter(a)
    b = Counter(b)
    a.subtract(b)
    return sum(map(abs, a.values()))


a = input()

b = input()

res = makeAnagram(a, b)

print(str(res) + '\n')
