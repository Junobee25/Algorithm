# 동전의 개수 N
N = int(input())
arr = list(map(int,input().split()))
M = int(input())
res = 2147000000
arr.sort(reverse=True) # 내림차순부터 적용해서 깊이 들어가지 않게

def DFS(L,sum):
    global res
    if L > res:  # 재귀 깊이 조절
        return
    if sum > M: 
        return
    if sum == M:
        if L < res:
            res = L
    else:  # (1,1) (1,1+1),(1,1+1+1) -> (1,1+1+2) (1,1+1+5) stack 답이 없으면 최근 노드로 돌아오고 탐색
        for i in range(N):
            DFS(L+1,sum+arr[i])
DFS(0,0)
print(res)