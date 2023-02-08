from collections import deque
# TEST CASE
T = int(input())
# 방문리스트 돌명서 방문하지 않은 요소는 bfs하고 count +1
def bfs(V):
    q = deque()
    q.append(V)
    visited[V] = 1 # 방문체크
    while q:
        k = q.popleft()
        for i in range(1,N+1):
            if visited[i] == 0 and matrix[k][i] == 1:
                visited[i] = 1
                q.append(i)
# 인덱스가 행 요소가 열인 연결리스트 만들기
for i in range(T):
    # 노드갯수
    N = int(input())
    cnt = 0
    arr = list(map(int,input().split()))
    arr = [0] + arr 
    matrix = [[0]*(N+1) for _ in range(N+1)]
    visited = [0 for _ in range(N+1)] # 방문리스트 1차원배열 Test case 돌때마다 초기화
    for x in range(1,N+1):
        matrix[x][arr[x]] = matrix[arr[x]][x] = 1 # 연결리스트
    for j in range(1,N+1):
        if visited[j] == 0:
            bfs(j)
            cnt += 1
    print(cnt)
