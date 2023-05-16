# 딱 KT코테에서 문제를 접한 느낌
# 규칙성이 안떠오르고
# 어떻게 풀어야 할지 잘 모르겠음
# 2023-05-16 새벽

# 2023-05-16 저녁
from collections import deque
A,B,C = map(int,input().split())

# 3차원 배열
visited = [[[False]*201 for _ in range(201)] for _ in range(201)]
result = []
def bfs():
    a,b,c = 0,0,C
    q = deque()
    q.append((a,b,c))
    visited[a][b][c] = True
    while q:
       a1,b1,c1 = q.popleft()
       if a1 == 0:
           result.append(c1)
        # c -> b
       water = min(c1,B-b1)
       if visited[a1][b1+water][c1-water] == False:
           q.append((a1,b1+water,c1-water))
           visited[a1][b1+water][c1-water] = True
        # c -> a
       water = min(c1,A-a1)
       if visited[a1+water][b1][c1-water] == False:
          q.append((a1+water,b1,c1-water))
          visited[a1+water][b1][c1-water] = True
        # b -> a
       water = min(b1,A-a1)
       if visited[a1+water][b1-water][c1] == False:
           q.append((a1+water,b1-water,c1))
           visited[a1+water][b1-water][c1] = True
        # b -> c
       water = min(b1,C-c1)
       if visited[a1][b1-water][c1+water] == False:
           q.append((a1,b1-water,c1+water))
           visited[a1][b1-water][c1+water] = True
        # a -> c
       water = min(a1,C-c1)
       if visited[a1-water][b1][c1+water] == False:
           q.append((a1-water,b1,c1+water))
           visited[a1-water][b1][c1+water]
       water = min(a1,B-b1)
       if visited[a1-water][b1+water][c1] == False:
           q.append((a1-water,b1+water,c1))
           visited[a1-water][b1+water][c1] = True
bfs()
result = set(result)
result = list(result)
result.sort()
for i in result:
    print(i, end = " ")