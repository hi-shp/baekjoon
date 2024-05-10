import sys
input = sys.stdin.readline
N = int(input())
a = [int(input()) for _ in range(N)] #입력 리스트
b = []                 #스택 리스트
result = []
def push(i):
    b.append(i+1)
    result.append('+')
def pop():
    b.remove(b[len(b)-1])
    result.append('-')
for x in a:
    if x == a[0]:                     #첫 번째 수
        for i in range(x):
            push(i)
            P = max(b)                #P = 인풋 최대 수
        pop()
    else:                             #첫 번째가 아니면
        if x > P-1:                 #스택 마지막 수가 x보다 작으면
            for i in range(P, x, 1):  #그 차이만큼 +출력
                push(i)
                P = max(b)
            pop()
        elif x == P-1:              #같으면
            pop()
        else:                               #스택 마지막 수가 x보다 크면
            if x == b[len(b)-1]:          #다음 수가 이전 수보다 2이상 작지 않으면
                pop()
            else:                           #2이상 작으면
                print('NO')
                del result[:]
                break
for x in result:
    print(x, end='\n')