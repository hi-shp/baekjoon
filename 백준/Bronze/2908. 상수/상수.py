A, B = map(str, input().split())
a, b = list(str(A)), list(str(B))
a, b = reversed(a), reversed(b)
a = ''.join(map(str, a))
b = ''.join(map(str, b))
a, b = int(a), int(b)
print(max(a, b))