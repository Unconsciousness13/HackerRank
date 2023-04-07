def count_substring(string, sub_string):
    counter = 0
    for i in range(0, len(string)):
        ocurence = string[i:len(sub_string) + i]
        if sub_string == ocurence:
            counter += 1
    return counter


string = input()
sub_string = input()
print(count_substring(string, sub_string))
