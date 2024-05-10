N, M = map(int, input().split())
a = [i for i in range(1, N+1)]
for _ in range(M):
    x, x1 = map(int, input().split())
    a[x-1:x1] = reversed(a[x-1:x1])
print(*a)