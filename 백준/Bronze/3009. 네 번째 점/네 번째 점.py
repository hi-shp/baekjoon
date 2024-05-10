A, B = list(),list()
for i in range(3):
    a, b = map(int, input().split())
    A.append(a), B.append(b)
    A.sort(reverse=True), B.sort(reverse=True)
def K(A):
    if A[0] == A[1]:
        x = A[2]
    else:
        x = A[0]
    return x
print(K(A), K(B))