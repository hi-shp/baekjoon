T = int(input())
for i in range(T):
    A = B = 0
    for _ in range(9):
        a, b = map(int, input().split())
        A += a
        B += b
    if A > B:
        print('Yonsei')
    elif A < B:
        print('Korea')
    elif A == B:
        print('Draw')