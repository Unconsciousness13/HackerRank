def mutate_string(string, position, character):
    result = ""
    for i in range(len(string)):
        if i == position:
            result += character
        else:
            result += string[i]

    return result

    # other
    # i, c = input().split()
    # s_new = mutate_string(s, int(i), c)
    # print(s_new)


string = input()
position = int(input())
character = input()
mutate_string(string, position, character)
