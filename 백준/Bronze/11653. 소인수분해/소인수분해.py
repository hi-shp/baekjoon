N = int(input())
if N != 1:
    a = 2
    while a < N:
        count = 0
        while N % a == 0:
            count += 1
            N /= a
            if N % a != 0:
                for _ in range(count):
                    print(a)
                break
        a += 1
    if a == N:
        print(a)