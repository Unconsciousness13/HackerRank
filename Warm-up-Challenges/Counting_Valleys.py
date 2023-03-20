def countingValleys(steps, path):
    deepth = 0
    highest = 0
    for i in range(steps):
        if path[i] == "U":
            deepth += 1
        else:
            deepth -= 1
        if deepth == 0 and path[i] == "U":
            highest += 1
    return highest


steps = int(input().strip())

path = input()

result = countingValleys(steps, path)

print(str(result) + '\n')
