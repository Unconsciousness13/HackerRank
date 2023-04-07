input1 = int(input())

c = 1
i = 0
while i < input1:
    print(("H"*c).rjust(input1+i, ' '))
    c += 2
    i = i+1
i = 0
x = input1*2-1
while i < input1+1:
    print(("H"*input1).center(x, " ")+(" ") *
          (input1*2+1)+("H"*input1).center(x, " "))
    i = i+1
i = 0
while i < (input1+1)//2:
    print(("H"*(input1*5)).center(((input1*5)+(input1-1)), " "))
    i += 1
i = 0
x = input1*2-1
while i < input1+1:
    print(("H"*input1).center(x, " ")+(" ") *
          (input1*2+1)+("H"*input1).center(x, " "))
    i = i+1
i = 0
x = 1
c = input1*2-1
while i < input1:
    print(("H"*c).rjust(((input1*5)+(input1-x)), " "))
    i = i+1
    c -= 2
    x = x+1
