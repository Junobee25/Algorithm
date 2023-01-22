import sys
input = sys.stdin.readline
def DFS(L):  
    global cnt
    if L == M: # DFS L != M # DFS L == M
        for j in range(M):
            print(res[j],end=" ")
            print()
            cnt += 1  # if문 실행 후 DFS(2) 가 끝나고 pop 후 DFS(1)로 복귀 이때 i == 1 , i == 3 
    else:
        for i in range(1,N+1): # i == 3 때 까지 for문이 돌고 끝나면 DFS(0)으로 복귀 (i == 1)
            res[L] = i # res[0] = 1 res[1] = 1 i == 2 일때 부터 다시 시작 res[1] = 2 rew[1] = 3
            DFS(L+1) # DFS(1) 호출 # DFS(2) 호출


N,M = map(int,input().split())
res = [0]*M # 조합들이 스택에 쌓이고 DFS함수를 통해 출력되는 루틴
cnt = 0
DFS(0)
print(cnt)