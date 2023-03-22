def countApplesAndOranges(s, t, a, b, apples, oranges):
    s, t = first_multiple_input
    s, t = int(s), int(t)
    apple_tree = a
    orange_tree = b
    apples = apples
    oranges = oranges
    apple_falls = 0
    orange_falls = 0

    for apple in apples:
        if s <= int(apple) + apple_tree <= t:
            apple_falls += 1

    for orange in oranges:
        if s <= int(orange) + orange_tree <= t:
            orange_falls += 1

    print(apple_falls)
    print(orange_falls)


first_multiple_input = input().rstrip().split()

s = int(first_multiple_input[0])

t = int(first_multiple_input[1])

second_multiple_input = input().rstrip().split()

a = int(second_multiple_input[0])

b = int(second_multiple_input[1])

third_multiple_input = input().rstrip().split()

m = int(third_multiple_input[0])

n = int(third_multiple_input[1])

apples = list(map(int, input().rstrip().split()))

oranges = list(map(int, input().rstrip().split()))

countApplesAndOranges(s, t, a, b, apples, oranges)
