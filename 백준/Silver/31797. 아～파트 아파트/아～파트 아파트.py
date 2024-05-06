import sys
N,M=map(int,sys.stdin.readline().split())
dic={}
all=[]
for i in range(1,M+1):
    a,b=map(int,sys.stdin.readline().split())
    dic[a]=i
    dic[b]=i
    all.append(a),all.append(b)
    all.sort()
if N%len(all)!=0:
    print(dic[all[N%len(all)-1]])
else:
    print(dic[all[len(all)-1]])