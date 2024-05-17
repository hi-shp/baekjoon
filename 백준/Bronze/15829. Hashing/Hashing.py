import sys
input = sys.stdin.readline
n = int(input())
total = 0
a = input().strip()
for i in range(len(a)):
    total += (ord(a[i])-96)*(31**i)
print(total%1234567891)