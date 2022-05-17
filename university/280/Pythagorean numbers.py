def checknum(a,b,c):
    a **= 2
    b **= 2
    c **= 2
    if a+b == c:
        return True
    elif a+c == b:
        return True
    elif b+c == a:
        return True
    return False
a = int(input())
b = int(input())
c = int(input())
if checknum(a,b,c):
    print('YES')
else:
    print('NO')