

def dayOfProgrammer(year):
    day = 13
    if year < 1918:

        if year % 4 == 0:
            day = 12
        else:
            day = 13

    elif year > 1918:

        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            day = 12
        else:
            day = 13
    else:
        day = 26

    res = str(f"{day}.09.{year}")
    return res


year = int(input().strip())

result = dayOfProgrammer(year)

print(result + '\n')
