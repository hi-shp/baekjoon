T = int(input())
for _ in range(T):
    a = list(input())
    sum = 0
    k = 0
    for x in a:
        if x == 'O':
            k += 1
            sum += k
        else:
            k = 0
    print(sum)