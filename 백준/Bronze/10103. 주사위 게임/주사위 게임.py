T = int(input())
A = B = 100
for _ in range(T):
    a, b = map(int, input().split())
    if a > b:
        B -= a
    elif b > a:
        A -= b
print(A, B, sep='\n')