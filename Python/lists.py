N = int(input())
the_arr = []
for i in range(N):
    com = input().split()
    command = com[0]
    if command == "insert":
        n = int(com[1])
        index = int(com[2])
        the_arr.insert(n, index)
    elif command == "print":
        print(the_arr)
    elif command == "append":
        n = int(com[1])
        the_arr.append(int(n))
    elif command == "remove":
        the_arr.remove(int(com[1]))
    elif command == "sort":
        the_arr.sort()
    elif command == "pop":
        the_arr.pop()
    elif command == "reverse":
        the_arr.reverse()
