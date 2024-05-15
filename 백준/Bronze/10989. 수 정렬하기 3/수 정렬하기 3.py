import sys
input = sys.stdin.readline
a = [0 for i in range(10000)]
for _ in range(int(input())):
    x = int(input())
    a[x-1] += 1
for i in range(len(a)):
    if a[i] != 0:
        for _ in range(a[i]):
            print(i+1)