import sys
a,b,c,d,e,f = map(int, sys.stdin.readline().split())
x, y = [i for i in range(-999, 1000)], [i for i in range(-999, 1000)]
for k in x:
    for h in y:
        if k*a + h*b == c:
            if k*d + h*e == f:
                print(k,h)
                break