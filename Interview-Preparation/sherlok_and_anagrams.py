def sherlockAndAnagrams(s):
    # Write your code here
    # Get all substrings as a list of sorted string
    sorted_substrings = []
    # Get count of each sorted substring
    count_dict = {}
    for i in range(len(s)):
        for j in range(i, len(s)):
            x = "".join(sorted(s[i: j + 1]))
            if x not in count_dict:
                count_dict[x] = 1
            else:
                count_dict[x] += 1
            sorted_substrings.append(x)
    # Get count of anagram pairs
    count = 0
    for x in count_dict:
        if count_dict[x] > 1:
            count += count_dict[x] * (count_dict[x] - 1) // 2
    return count


q = int(input().strip())

for q_itr in range(q):
    s = input()

    result = sherlockAndAnagrams(s)

    print(str(result) + '\n')
