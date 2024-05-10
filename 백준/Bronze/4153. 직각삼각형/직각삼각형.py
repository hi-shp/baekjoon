import sys
input = sys.stdin.readline
while True:
    try:
        a,b,c=map(int,input().split())
        while a != 0:
            A = [a,b,c]
            A = sorted(A, reverse=True)
            a = A[0]
            b = A[1]
            c = A[2]
            if a**2 == b**2 + c**2:
                print('right')
            else:
                print('wrong')
            break
    except:
        break