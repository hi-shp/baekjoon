T = int(input())
for _ in range(T):
    N, a = map(int, input().split())
    A = str(a)
    x = int(A[0])
    L = len(A)
    result =[]
    while True:
        k = 0
        for i in range(L):
            k += x*(10**i)
        if k <= a:
            a -= k
            result.append(str(k))
        else:
            if x != 1:
                x -= 1
                continue
            else:
                x = 9
                L -= 1
                continue
        A = str(a)
        x = int(A[0])
        L = len(A)
        if a == 0:
            break
    print(len(result))
    print(' '.join(result))