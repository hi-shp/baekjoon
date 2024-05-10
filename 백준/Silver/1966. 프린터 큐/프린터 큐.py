N = int(input())
for _ in range(N):
    N, M = map(int, input().split())
    a = [0 for _ in range(1, N+1)]
    a[M] = 1
    b = list(map(int, input().split()))
    k = 0
    while True:
        if a[0] != 1:
            if b[0] != max(b):
                a.append(a.pop(0))
                b.append(b.pop(0))
            else:
                a.remove(a[0]), b.remove(b[0])
                k += 1
        else:
            if b[0] == max(b):
                k += 1
                break
            else:
                a.append(a.pop(0))
                b.append(b.pop(0))
    print(k)