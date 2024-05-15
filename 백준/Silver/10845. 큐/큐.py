import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
result = []
que = deque(result)
for _ in range(T):
    a = list(input().split())
    if len(a) == 2:
        que.append(a[1])
    else:
        if a[0] == 'pop':
            print(que.popleft() if que else -1)
        elif a[0] == 'size':
            print(len(que))
        elif a[0] == 'empty':
            print(0 if que else 1)
        elif a[0] == 'front':
            print(que[0] if que else -1)
        elif a[0] == 'back':
            print(que[-1] if que else -1)