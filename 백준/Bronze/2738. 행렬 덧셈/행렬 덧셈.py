N, M = map(int, input().split())
a, b = [], []
for _ in range(N):
    a.append(list(map(int, input().split())))
for _ in range(N):
    b.append(list(map(int, input().split())))
for j in range(N):
    for i in range(M):
        a[j][i] += b[j][i]
for j in range(N):
    for i in range(M):
        print(a[j][i], end=' ')
    print()