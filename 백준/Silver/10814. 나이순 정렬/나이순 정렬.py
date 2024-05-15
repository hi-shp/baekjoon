import sys
input = sys.stdin.readline
N = int(input())
list = []
for _ in range(N):
    a, b = input().split()
    a = int(a)
    list.append([a, b])
list.sort(key=lambda x: x[0])
for x in list:
    print(*x)