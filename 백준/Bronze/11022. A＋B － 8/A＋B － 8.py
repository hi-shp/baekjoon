T = int(input())
for T in range(1, T+1):
    a,b = map(int, input().split())
    print("Case #"+str(T)+":",a,"+",b,"=",a+b)