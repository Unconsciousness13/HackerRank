from functools import cmp_to_key


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def comparator(x, y):
        if x.score < y.score:
            return 1
        if x.score > y.score:
            return -1
        if x.name > y.name:
            return 1
        if x.name < y.name:
            return -1
        return 0

    def __repr__(self):
        return f"{self.name} {self.score}"


n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)

data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)
