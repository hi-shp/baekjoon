N, M = map(int, input().split())
L = list()
for i in range(N):
    L.append(0)
for _ in range(M):
    A, B, K = map(int, input().split())
    a = 0
    for i in range(N):
        if i+1 == A:
            a = K
            for j in range(A-1, B):
                L[j] = a
for x in L:
    print(x, end=' ')