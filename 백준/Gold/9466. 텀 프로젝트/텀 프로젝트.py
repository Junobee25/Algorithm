# # bfs를 통해 노드를 탐색해보자
# # 그냥 bfs를 돌면 사이클 그룹을 돌수도 있고 그냥 트리를 돌수있다.
# # 일단 사이클인지 아닌지를 먼저 판단하는게 우선일 것 같다.
# # 마지막으로 탐색한 노드가 처음 체크한 노드이면 사이클임
# # 마지막으로 탐색한 노드가 처음 체크한 노드가 아니면 사이클이 아니고 그룹이 될 수없음
# # 그룹이 될수없는 그래프를 탐색할 때마다 노드를 count를 시켜주면 그게 정답?? 설계완료

# # 그래프가 사각형 사이클일때 첫방문한 노드랑 마지막 노드가 연결안되있을 수도있으니
# # 마지막 노드의 연결리스트안에 첫방문한 노드가 들어있으면 사이클이다 라고 풀수 없다.
# from collections import deque
# import sys
# input = sys.stdin.readline
# def bfs(V):
#     global cnt
#     visited[V] = 1
#     q = deque()
#     q.append(V)
#     cycle = [V]
#     while q:
#         k = q.popleft()
#         for i in range(1,n+1):
#             if visited[i] == 0 and matrix[k][i] == 1: # 방문을 안한노드고 연결되어있다면
#                 q.append(i)
#                 cycle.append(i) # 연결된 노드 추가 (탐색이 끝나고 cycle 마지막)
#     if cycle[-1] != cycle[-2]:
#         cnt += len(cycle)
        
# T = int(input())
# for _ in range(T):
#     n = int(input())
#     visited = [0 for _ in range(n+1)] # 방문 리스트
#     ch = list(map(int,input().split())) # 선택 배열 생성 인덱스 -> 값 (선택과정)
#     ch = [0] + ch
#     matrix = [[0]*(n+1) for _ in range(n+1)]
#     cnt = 0
#     for i in range(1,n+1):
#         matrix[i][ch[i]] = matrix[ch[i]][i] = 1
#     for j in range(1,n+1):
#         if visited[j] != 1:
#             bfs(j)
#     print(cnt)
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    ch = list(map(int,input().split()))

    visited = [False for _ in range(n)]
    cycle = [False for _ in range(n)]

    for i in range(n): # node 번호는 i로 설정
        if visited[i]: # 만약에 방문한 노드면 continue
            continue
        visited[i] = True # 방문하지 않으면 체크
        cur = i # i를 cur로 설정하고 order리스트를 만들어 cur을 담아줌
        order = [cur]
        while True: 
            next = ch[cur] - 1
            if visited[next]: # 방문 체크 되있으면
                if next not in order: # 없으면 이미 탐색 완료 노드
                    break
                else: # order안에 next가 들어있으면 싸이클 발견??
                    j = order.index(next)
                    for k in range(j,len(order)):
                        cycle[order[k]] = True # 싸이클 발견후 order안에 next위치를 찾아 
                    break # 끝까지 탐색하며 해당 노드의 싸이클 여부를 True로 설정
            visited[next] = True # while문에서 next 노드를 꺼내와서 next노드가 방문 체크 안되있으면
            order.append(next) # 방문 체크및 order 리스트 추가
            cur = next
    print(n-sum(cycle))