from collections import deque

N,M = map(int,input().split())

cnt_visited = [-1 for i in range(100001)]  ## 노드와 간선 갯수 초기화 해줄 트리


def bfs(V):
    queue = deque()
    queue.append(V)
    cnt_visited[V] = 0
    while queue: ## 원소가 다 pop될때까지 순회
        now_Node = queue.popleft()
        if now_Node + 1 <= 100000 and cnt_visited[now_Node+1] == -1: ## 방의갯수 초과 x 방문하지 않은 방
            queue.append(now_Node +1)
            cnt_visited[now_Node+1] = cnt_visited[now_Node] + 1  ## 거쳐간 너비 1++
        if now_Node -1 >= 0 and cnt_visited[now_Node-1] == -1:
            queue.append(now_Node-1)
            cnt_visited[now_Node-1] = cnt_visited[now_Node] +1  ## 거쳐간 너비 1++
        if now_Node*2 <= 100000 and cnt_visited[now_Node*2] == -1 :
            queue.append(now_Node*2)
            cnt_visited[now_Node*2] = cnt_visited[now_Node] + 1 ## 거쳐간 너비 1++

bfs(N)
print(cnt_visited[M])

