a,b = map(int,input().split())
def E(a, b):
    while b != 0:
        [a, b] = [b, a%b]
    return a
print(E(a, b))
print(round(a*b/E(a,b)))