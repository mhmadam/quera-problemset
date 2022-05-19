def printsq2(n):
    i = 1
    while i <= n//2:
        if i == 1:
            for j in range(n):
                print('#',end='')
        else:
            for j in range(i):
                if not (j == i-1 or j == 0):
                    print(' ',end='')
                else:
                    print('#',end='')
            for j in range(i,n//2+n%2,1):
                print(' ',end='')
            for j in range(i,n//2,1):
                print(' ',end='')
            for j in range(i):
                print('#',end='')
        i += 1
        print()
    if n%2:
        for j in range(n):
            if j == 0 or j >= n//2:
                print('#',end='')
            else:
                print(' ',end='')
        print()
    i -= 1
    while i >= 1:
        if i == 1:
            for j in range(n):
                print('#',end='')
        else:
            for j in range(i):
                if not (j == i-1 or j == 0):
                    print(' ',end='')
                else:
                    print('#',end='')
            for j in range(i,n//2+n%2,1):
                print(' ',end='')
            for j in range(i,n//2,1):
                print(' ',end='')
            for j in range(i):
                print('#',end='')
        i -= 1
        print()
n = int(input())
printsq2(n)
