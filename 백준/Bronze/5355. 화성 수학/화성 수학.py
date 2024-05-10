T = int(input())

for _ in range(0, T):
    x = list(map(str, input().split()))
    a = float(x[0])
    for i in range(1, len(x)):
        if x[i] == '@':
            a *= 3
        elif x[i] == '%':
            a += 5
        elif x[i] == '#':
            a -= 7
    print('{:.2f}'.format(a))