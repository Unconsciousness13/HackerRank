def timeConversion(s):
    # res = ''
    # daytimeConv = s[-2]
    # hourConv1 = s[0]
    # hourConv2 = s[1]
    # if daytimeConv == "P":
    #     if hourConv1 == "0":
    #         if hourConv2 == "1":
    #             res = "13" + s[2:-2]
    #         elif hourConv2 == "2":
    #             res = "14" + s[2:-2]
    #         elif hourConv2 == "3":
    #             res = "15" + s[2:-2]
    #         elif hourConv2 == "4":
    #             res = "16" + s[2:-2]
    #         elif hourConv2 == "5":
    #             res = "17" + s[2:-2]
    #         elif hourConv2 == "6":
    #             res = "18" + s[2:-2]
    #         elif hourConv2 == "7":
    #             res = "19" + s[2:-2]
    #         elif hourConv2 == "8":
    #             res = "20" + s[2:-2]
    #         elif hourConv2 == "9":
    #             res = "21" + s[2:-2]
    #     if hourConv1 == "1":
    #         if hourConv2 == "0":
    #             res = "22" + s[2:-2]
    #         elif hourConv2 == "1":
    #             res = "23" + s[2:-2]
    #         elif hourConv2 == "2":
    #             res = "12" + s[2:-2]
    # elif daytimeConv == "A":
    #     if hourConv1 == "1":

    #         if hourConv2 == "2":
    #             res = "00" + s[2:-2]
    #     else:
    #         res = s[:-2]

    # return res

    if s[0:2] == '12' and s[8:] == "AM":
        return "00"+s[2:8]
    elif s[8:] == "PM":
        return str((int(s[0:2]) % 12) + 12)+s[2:8]
    else:
        return s[:8]


s = input()

result = timeConversion(s)

print(result + "\n")
