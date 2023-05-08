import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#


def luckBalance(k, contests):
    important_contests = []
    unimportant_contests = []
    for contest in contests:
        if contest[1] == 1:
            important_contests.append(contest[0])
        else:
            unimportant_contests.append(contest[0])
    important_contests.sort(reverse=True)
    luck_balance = sum(unimportant_contests)
    for i in range(len(important_contests)):
        if i < k:
            luck_balance += important_contests[i]
        else:
            luck_balance -= important_contests[i]
    return luck_balance


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
