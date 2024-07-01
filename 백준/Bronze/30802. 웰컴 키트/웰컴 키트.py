N = int(input())
a = list(map(int, input().split()))
T, P = map(int, input().split())
k = 0
for x in a:
    if x>0 and x <= T:
        k += 1
    elif x%T == 0:
        k += x//T
    else:
        k += (x//T + 1)
print(k)
print(N//P, N%P)