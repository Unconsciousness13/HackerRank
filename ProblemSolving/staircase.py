def staircase(n):

    for i in range(n+1):
        if i > 0:
            spaces = n-i
            print(spaces*" " + "#" * i)

    # for i in range(n, 0, -1):
    #     if i > 0:
    #         spaces = " " * (i - 1)
    #         stairs = "#" * (n - i + 1)
    #         print(spaces + stairs)


n = int(input().strip())

staircase(n)
