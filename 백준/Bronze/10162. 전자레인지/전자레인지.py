T = int(input())
a=b=c = 0
while True:
    if T >= 300:
        a += T//300
        T = T%300
    elif T >= 60:
        b += T//60
        T = T%60
    else:
        c += T//10
        T = T%10
    if 0 < T and T < 10:
        print(-1)
        break
    elif T == 0:
        print(a, b, c)
        break