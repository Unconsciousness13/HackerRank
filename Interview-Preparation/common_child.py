def commonChild(s1, s2):
    letter_dict = {}
    for idx, letter in enumerate(s1):
        if letter not in letter_dict:
            letter_dict[letter] = [idx]
        else:
            letter_dict[letter].append(idx)
    arr = []
    for letter in s2:
        if letter in letter_dict:
            arr_size = len(arr)
            l_start_idx = 0
            for l_end_idx, letter_idx in enumerate(letter_dict[letter]):
                if (not arr) or (letter_idx > arr[-1]):
                    l_end_idx -= 1
                    arr.append(letter_idx)
                    break
            for i, idx in enumerate(arr[:arr_size]):
                if l_start_idx > l_end_idx:
                    break
                found = False
            for l_idx in range(l_start_idx, l_end_idx+1):
                letter_idx = letter_dict[letter][l_idx]
                if letter_idx > idx:
                    break
                if not found:
                    arr[i] = letter_idx
                    found = True
                l_start_idx += 1

    max_len = len(arr)
    return max_len


s1 = input()

s2 = input()

result = commonChild(s1, s2)

print(str(result) + '\n')
