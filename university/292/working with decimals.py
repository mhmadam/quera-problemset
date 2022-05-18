def chfloat(n):
    if not n == 0:
        n *= 1000
    else:
        n += 1000
    return str(int(n))[-3:]
n = int(input())
if n >= 1 and n <= 5:
    a = []
    av = 0
    for i in range(n):
        inp = float(input())
        a.append(inp)
        av += inp
    if not av == 0:
        av /= n
    a.sort()
    if n == 4:
        print('Max: '+str(int(a[n-1]))+'.'+str(chfloat(a[n-1])))
        print('Min: '+str(int(a[0]))+'.'+str(chfloat(a[0])))
        print('Avg: '+str(int(av))+'.'+str(chfloat(av)))
    else:
        print('Max: {:.3f}'.format(a[n-1]))
        print('Min: {:.3f}'.format(a[0]))
        print('Avg: {:.3f}'.format(av))
