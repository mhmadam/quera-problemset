def isprime(n):
    for i in range(2,int(n/2+1)):
        if n%i == 0:
            return False
    return True
def findprime(m,n):
    for i in range(m,n+1):
        if isprime(i) and not i == 1:
            print(i)
    return
a = int(input())
b = int(input())
if a >= b and b >= 1 and a <= 10000:
    findprime(b,a)
elif a <= b and a >= 1 and b <= 10000:
    findprime(a,b)
