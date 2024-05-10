T = int(input())
A = B = 0
for _ in range(T):
    a = str(input())
    if a == '1':
        A += 1
    else:
        B += 1
if A>B:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')