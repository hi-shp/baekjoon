N = int(input())
if N != 1:
    a = list(map(int, input().split()))
    a.sort()
    t = []
    x = a[0]
    k = 1
    for i in range(N):
        if a[i] >= 2*x:
            k += 1
            x = a[i]
    t.append(k)
    print(min(t))
else:
    print(1)