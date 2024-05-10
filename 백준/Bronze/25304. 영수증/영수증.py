Total = int(input())
T = int(input())
k = 0
for _ in range(T):
    a,b = map(int,input().split())
    k += a*b
if k == Total:
    print("Yes")
else:
    print("No")