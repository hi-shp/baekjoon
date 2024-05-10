T = int(input())

for _ in range(T):
    a, b = input().split()
    for x in b:
        print(x*int(a), end='')
    print()