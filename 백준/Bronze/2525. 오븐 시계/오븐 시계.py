a,b = map(int,input().split())
c = int(input())
if (b+c)//60 < 1 :
    min = b + c
elif (b+c)%60 == 0 :
    min = 0
    a = a+(b+c)//60
else :
    min = (b+c)%60
    a = a+(b+c)//60
if a >= 24 :
    a = a%24
print(a,min)