import sys
input = sys.stdin.readline
T = int(input())
stack = []
for _ in range(T):
    a = list(input().split())
    if len(a) == 2:
        stack.append(a[1])
    else:
        if a[0]=='pop':
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif a[0]=='size':
            print(len(stack))
        elif a[0]=='empty':
            if stack:
                print(0)
            else:
                print(1)
        elif a[0]=='top':
            if stack:
                print(stack[-1])
            else:
                print(-1)