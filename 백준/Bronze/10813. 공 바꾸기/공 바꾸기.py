N, M = map(int, input().split())
A = list()
for i in range(N):
    A.append(i+1)
for _ in range(M):
    a, b = map(int, input().split())
    k = A[a-1]
    f = A[b-1]
    A[a-1] = f
    A[b-1] = k
for x in A:
    print(x, end=' ')