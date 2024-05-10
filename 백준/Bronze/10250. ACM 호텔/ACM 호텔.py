T = int(input())
for _ in range(T):
    H, W, n = map(int, input().split())
    x = 0
    if n%H == 0:
        x += 100 * H
        x += n//H
    else:
        x += 100 * (n % H)
        x += (n//H) +1
    print(x)