import sys
input = sys.stdin.readline
arr = [True for _ in range(10001)]
for i in range(2,101):
    if arr[i] == True:
        for j in range(i+i,10001,i):
            arr[j] = False
T = int(input().rstrip())
for i in range(T):
    N = int(input().rstrip())
    # 반으로 쪼개서 차이를 벌리는 아이디어
    a ,b = N//2,N//2
    while True :
        if arr[a] and arr[b]:
            print(a,b)
            break
        else:
            a -= 1
            b +=1
