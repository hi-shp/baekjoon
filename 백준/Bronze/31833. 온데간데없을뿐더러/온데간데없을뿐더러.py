N = int(input())
a = list(map(str, input().split()))
b = list(map(str, input().split()))
print(min(int(''.join(a)), int(''.join(b))))