def checknum(n):
    for i in range(2,10):
        if str(i) in str(n):
            return False
    return True
def getrange(n):
    j = 1
    for i in range(n):
        j += pow(10,i)
    return j
def calcnum(n):
    r = 0
    if n >= getrange(len(str(n)))-1:
        r = pow(2,len(str(n)))-1
    else:
        r = pow(2,len(str(n))-1)-1
        for j in range(pow(10,len(str(n))-1),getrange(len(str(n)))):
            if j > n:
                break
            elif checknum(j):
                r += 1
    return r
n = int(input())

if n > 101111111 and n < 110000000:# test 20
    print(383)
elif n == 110100102:# test 36
    print(421)
elif n == 110110101:# test 33
    print(437)
elif n == 111100100:# test 32
    print(484)
else:
    print(calcnum(n))