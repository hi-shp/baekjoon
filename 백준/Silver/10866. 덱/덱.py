import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
result = []
deque = deque(result)
for _ in range(T):
    a = list(input().split())
    if len(a) == 2:
        if a[0] == 'push_front':
            deque.appendleft(a[1])
        elif a[0] == 'push_back':
            deque.append(a[1])
    else:
        if a[0] == 'pop_front':
            print(deque.popleft() if deque else -1)
        elif a[0] == 'pop_back':
            print(deque.pop() if deque else -1)
        elif a[0] == 'size':
            print(len(deque))
        elif a[0] == 'empty':
            print(0 if deque else 1)
        elif a[0] == 'front':
            print(deque[0] if deque else -1)
        elif a[0] == 'back':
            print(deque[-1] if deque else -1)