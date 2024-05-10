T = int(input())
Q1 = Q2 = Q3 = Q4 = AXIS = 0
for _ in range(T):
    a, b = map(int, input().split())
    if a == 0 or b == 0:
        AXIS += 1
    elif a > 0:
        if b > 0:
            Q1 += 1
        else:
            Q4 += 1
    else:
        if b > 0:
            Q2 += 1
        else:
            Q3 += 1
Q = [Q1, Q2, Q3, Q4, AXIS]
for i in range(4):
    print("Q",i+1,": ",Q[i], sep='')
print("AXIS:",AXIS)