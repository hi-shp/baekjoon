import sys
input = sys.stdin.readline
def Up(num):
    if (num - int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)
n = int(input())
if n == 0:
    print(0)
else:
    a = []
    for i in range(n):
        a.append(int(input()))
    a.sort()
    border = Up(n * 0.15)
    print(Up(sum(a[border:n - border]) / len(a[border:n - border])))