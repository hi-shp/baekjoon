t = int(input())
for _ in range(t):
    k = list(map(int,input().split()))
    a = sorted(k)
    a0 = a[0]
    a1 = a[1]
    def gcd(a, b):
        while b > 0:
            a, b = b, a % b
        return a
    def lcm(a, b):
        return a * b / gcd(a, b)
    print(format(lcm(a0, a1), '.0f'))