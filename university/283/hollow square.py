def printsq(a,b,c):
    d = a-b
    for j in range(b,a,2):
        for i in range(a):
            print(c,end=' ')
        print()
    for i in range(d//2,a-d//2):
        for j in range(b,a,2):
            print(c,end=' ')
        for j in range(b):
            print(' ',end=' ')
        for j in range(b,a,2):
            print(c,end=' ')
        print()
    for j in range(b,a,2):
        for i in range(a):
            print(c,end=' ')
        print()
a = int(input())
b = int(input())
if a <= b:
    print('Wrong order!')
else:
    if (a-b)%2 == 0:
        printsq(a,b,'*')
    else:
        print('Wrong difference!')