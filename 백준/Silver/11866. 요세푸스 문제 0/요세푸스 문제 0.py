from collections import deque
N, K = map(int, input().split())
a = [i for i in range(1, N + 1)]
a = deque(a)
result = []
for _ in range(N):
    a.rotate(-(K-1))
    result.append(a.popleft())
print('<', end='')
print(*result, sep=', ', end='')
print('>')