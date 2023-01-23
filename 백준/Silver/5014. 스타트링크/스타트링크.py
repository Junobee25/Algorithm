from collections import deque
F, S, G, U, D = map(int, input().split())
visited = [-1 for _ in range(F+1)]


def BFS(V):
    queue = deque()
    queue.append(V)
    visited[V] = 0
    while queue:
        Node = queue.popleft()
        if Node + U <= F and visited[Node+U] == -1:
            queue.append(Node+U)
            visited[Node+U] = visited[Node] + 1
        if Node - D >= 1 and visited[Node-D] == -1:
            queue.append(Node-D)
            visited[Node-D] = visited[Node] + 1


BFS(S)
if visited[G] == -1:
    print("use the stairs")
else:
    print(visited[G])
