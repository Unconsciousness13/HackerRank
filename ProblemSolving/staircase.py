def staircase(n):

    for i in range(n+1):
        if i > 0:
            spaces = n-i
            print(spaces*" " + "#" * i)


n = int(input().strip())

staircase(n)
