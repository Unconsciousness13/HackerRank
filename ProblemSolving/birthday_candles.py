def birthdayCakeCandles(candles):
    searching_num = max(candles)
    counter = 0
    for n in candles:
        if n == searching_num:
            counter += 1
    return counter


candles_count = int(input().strip())

candles = list(map(int, input().rstrip().split()))

result = birthdayCakeCandles(candles)

print(str(result) + '\n')
