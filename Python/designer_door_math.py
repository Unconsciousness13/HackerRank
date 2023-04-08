n, m = list(map(int, input().split()))

a = par = ""
for i in range(n):
    if i == n//2:
        a = 'WELCOME'
    elif i < n//2:
        if a == "":
            par = '.|.'
            a = par
        else:
            par += '.|..|.'
            a = par
    else:
        if i == (n//2+1):
            a = par
        else:
            par = par[6::]
            a = par
    print(a.center(m, '-'))
