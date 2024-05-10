T = int(input())
A = set(list(map(int, input().split())))
M = max(A)
a = [False, False]+[True]*(M-1)
b = []
for i in range(2, M+1):
    if a[i]:
        b.append(i)
        for j in range(2*i, M+1, i):
            a[j] = False
k = 0
for x in A:
    if x in b:
        k += 1
print(k)