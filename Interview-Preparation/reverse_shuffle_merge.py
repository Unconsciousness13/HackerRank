import os


def reverseShuffleMerge(s):
    if len(s) < 3:
        return s[0]

    l2, r26 = len(s) // 2, range(26)
    counts, ord_a, req = [0 for _ in r26], ord("a"), [0 for _ in r26]

    for i in range(len(s)):  # Get character counts
        counts[ord(s[i]) - ord_a] += 1

    # Halve the character counts to get the required counts for string A
    for i in r26:
        req[i] = counts[i] // 2

    stack = [None for _ in range(l2)]  # Build up the smallest A using stack
    ch, stack_i = ord(s[-1]) - ord_a, -1
    counts[ch], index, l2, old_end = counts[ch] - 1, len(s) - 1, l2 - 1, ch

    while True:
        if req[ch]:  # Check if the current ch is required
            """ Check if it's possible to construct a lexicographically
            smaller string A """
            while ch < old_end and req[old_end] + 1 <= counts[old_end]:
                req[old_end], stack_i = req[old_end] + 1, stack_i - 1
                if stack_i == -1:
                    break
                old_end = stack[stack_i]

            req[ch], stack_i = req[ch] - 1, stack_i + 1
            stack[stack_i] = old_end = ch

        if stack_i < l2:  # Continue if the stack isn't full yet
            index -= 1
            ch = ord(s[index]) - ord_a
            counts[ch] -= 1

        else:  # The stack is full and we've found the optimal solution
            break

    return "".join(map(lambda x: chr(x + ord_a), stack))


s = input()

result = reverseShuffleMerge(s)

print(result + '\n')
