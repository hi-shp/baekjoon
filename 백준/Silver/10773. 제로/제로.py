import sys
input = sys.stdin.readline
N = int(input())
stack = []
for _ in range(N):
    a = int(input())
    if a != 0:
        stack.append(a)
    else: stack.pop()
print(sum(stack))