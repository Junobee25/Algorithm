import sys
input = sys.stdin.readline
n = int(input())
score = [list(map(int,input().split())) for _ in range(n)]
target = [[] for _ in range(n)]
visited = [-1 for _ in range(n)]
for i in range(n-1):
    for j in range(i+1,n):
        if score[i][0] >= score[j][0] and score[i][1] >= score[j][1] and score[i][2] >= score[j][2]:
            target[i].append(j)
        elif score[i][0] <= score[j][0] and score[i][1] <= score[j][1] and score[i][2] <= score[j][2]:
            target[j].append(i)
# 한 상어가 다른 상어를 두번 먹을 수 있기 때문에
# dfs 두번 호출

def dfs(x):
    for i in target[x]:
        if checked[i]:
            continue
        checked[i] = True
        if visited[i] == -1 or dfs(visited[i]):
            visited[i] = x
            return True
    return False
        

res = 0
for i in range(n):
    checked = [False for _ in range(n)]
    if dfs(i):
        res += 1
    checked = [False for _ in range(n)]
    if dfs(i):
        res += 1
print(n-res)