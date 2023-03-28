
def bonAppetit(bill, k, b):
    ana_eatet_sum_total = (sum(bill) - bill[k]) / 2

    overcharged = b - ana_eatet_sum_total

    if 0 == int(overcharged):
        return print("Bon Appetit")
    else:
        return print(int(overcharged))


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

k = int(first_multiple_input[1])

bill = list(map(int, input().rstrip().split()))

b = int(input().strip())

bonAppetit(bill, k, b)
