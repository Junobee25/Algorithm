import sys
input = sys.stdin.readline
# N일동안 일이 딱 끝나야 됨
N = int(input().rstrip())
T = [0]
P = [0]
for i in range(N):
    a,b = map(int,input().split())
    T.append(a)
    P.append(b)
max_num = -21470000
# 상담을 완료하기 까지 걸리는 시간이 4일이면 4일후에 일을 시작할 수 있음
def dfs(L,s):
    global max_num
    if L == N+1: # 종료지점은 N+1
        if s > max_num:
            max_num = s
    
    else:
        if L + T[L] <= N+1: # 현재 날짜 + 걸리는 시간 이 N+1보다는 작거나 같아야지 진행가능
            dfs(L+T[L],s+P[L]) ## 사용한다. L = 현재 날짜 T[L] -> 걸리는 시간
        dfs(L+1,s) ## 사용 안한다 L = 현재 날짜 + 1


# 받을 수있는 금액이 최대여야 함
dfs(1,0)
print(max_num)






