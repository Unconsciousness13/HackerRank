def isValid(s):
    s_arr_frequence = []
    s_arr = [i for i in s]
    s_unique = set(s_arr)

    for i in s_unique:
        s_arr_frequence.append(s_arr.count(i))

    check = s_arr_frequence[0]
    count = 1
    for i in range(len(s_arr_frequence)-1):
        if check - s_arr_frequence[i+1] == 0:
            count += 1
    if count == len(s_arr_frequence) or count == len(s_arr_frequence)-1:
        return 'YES'
    else:
        return 'NO'
