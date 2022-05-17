def fact(x):
    if x <= 1:
        return 1
    else:
        return x*fact(x-1)
def calc1(n,k):
    c1 = fact(n)
    c2 = fact(k)*fact(abs(n-k))
    return c1/c2
def calc3(a,x,n):
    res = 0
    for k in range(n+1):
        r1 = calc1(n,k)
        r2 = pow(x,k)
        r3 = pow(a,n-k)
        res += r1*r2*r3
    return int(res)

inp = input()
while '  ' in inp:
    inp = inp.replace('  ',' ')
inp = inp.split(' ')
print(calc3(int(inp[0]),int(inp[1]),int(inp[2])))
