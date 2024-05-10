s = 1
for _ in range(3):
    a = int(input())
    s *= a
s = list(map(int, str(s)))
for i in range(10):
    print(s.count(i))