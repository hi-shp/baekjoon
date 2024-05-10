while True:
    a = int(input())
    if a != -1:
        k = 0
        L = list()
        for i in range(1,a):
            if a%i == 0:
                k += i
                L.append(str(i))
        if a == k:
            aL = ' + '.join(L)
            print(a,'=',aL)
        else:
            print(a,'is NOT perfect.')
    else:
        break