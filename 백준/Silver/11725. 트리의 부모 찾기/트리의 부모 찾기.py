from collections import deque
import sys
input = sys.stdin.readline
# 노드번호가 1인숫자 부터 출발하면서 너비우선 탐색을 합니다
def bfs(V):
    q = deque() # 노드를 FIFO 자료구조에 담아 popleft()된 노드를 기준으로 탐색합니다.
    q.append(V)
    # while문이 한번돌면 모든 노드 탐색이 끝남 탐색된 순서대로 방문체크해주면 됨
    while q:
       k = q.popleft() # q에서 빠진 노드는 부모 노드가 됩니다.
       for i in matrix[k]: # range를 쓰면안되겠다.
            if (visited[i] == 0):
                visited[i] = k
                q.append(i)
            
# 해당 노드번호와 연결된 인덱스번호(노드번호)에 부모 노드 할당

# 인덱스가 2부터 끝까지 출력

# 그래프 만들기
N = int(input().rstrip())
matrix = [[] for _ in range(N+1)]  # [[0]*(N+1) for _ in range(N+1)]  
visited = [0]*(N+1)
for i in range(1,N):
    a,b = map(int,input().split())
    matrix[a].append(b)
    matrix[b].append(a)
# 자식노드(인덱스) 부모노드(값) 리스트를 만들어 줍니다
# result = [0,1] + [0]*(N-1) # append가 아닌 할당을 해주기위해 이렇게 만듦
# 방문하지 않은 노드만 bfs돌려줌 (for문을 통해 자연스럽게 1부터 출발하게됩니다.)
bfs(1) # bfs가 for문을 통해 여러번 돌 필요가 없음
for i in range(2,N+1):
    print(visited[i])

# 처음 시도 matrix를 N*N으로 만들어줘서 메모리초과!
# 트리 형태니 append로 연결된 노드만 리스트에 넣어주기!
