from collections import deque
N = int(input())
a = [i for i in range(1, N+1)]
a = deque(a)
while len(a) != 1:
    a.popleft()
    a.append(a.popleft())
print(*a)