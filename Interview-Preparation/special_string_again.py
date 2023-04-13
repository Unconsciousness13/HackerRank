def substrCount(n, s):
    nsubs, nchars, ch = 1, 1, s[0]
    for i in range(1, n):
        if ch == s[i]:
            nchars += 1
            nsubs += nchars
        else:
            for j in range(i+1, min(n, i+1+nchars)):
                if s[j] != ch:
                    break
                nsubs += 1
            ch, nchars = s[i], 1
            nsubs += 1
    return nsubs
