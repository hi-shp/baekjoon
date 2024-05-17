N,K=map(int,input().split())
t=1
for i in range(N-K+1, N+1):
    t *= i
for i in range(1, K+1):
    t /= i
print(int(t))