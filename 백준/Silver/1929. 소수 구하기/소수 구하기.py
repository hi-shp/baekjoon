N, M = map(int,input().split())
a = [False, False]+[True]*(M-1)
b = []
for i in range(2, M+1):
    if a[i]:
        b.append(i)
        for j in range(2*i, M+1, i):
            a[j] = False
for x in b:
    if x >= N:
        if x <= M:
            print(x)