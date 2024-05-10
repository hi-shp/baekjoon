import sys
input = sys.stdin.readline
K, N = map(int, input().split())
a = [int(input()) for _ in range(K)]
start, end = 1, max(a)
while start <= end:
    mid = (start + end) // 2
    sum = 0
    for x in a:
        sum += x//mid
    if sum >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)