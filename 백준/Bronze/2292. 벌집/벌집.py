import sys
input = sys.stdin.readline
N = int(input())
if N == 1:
    print(1)
else:
    n = 1
    k = 1
    while True:
        if N == k+6*n:
            break
        elif k < N and N < k+6*n:
            break
        k += 6*n
        n += 1
    print(n+1)