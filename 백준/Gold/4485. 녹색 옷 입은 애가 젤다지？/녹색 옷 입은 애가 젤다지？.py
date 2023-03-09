import heapq
cnt = 0
while True:
    cnt += 1
    n = int(input())
    if n == 0:
        exit()
    matrix = [list(map(int, input().split())) for _ in range(n)]

    # (1,1)에서 (n,n)까지의 최소비용 구하기
    INF = int(1e9) 
    distance = [[INF] * n for _ in range(n)]

    dy = [-1,0,1,0]
    dx = [0,1,0,-1]

    # 다익스트라 알고리즘 구현
    def dijkstra(y, x):
        q = []
        heapq.heappush(q, (matrix[y][x], y, x))
        distance[y][x] = matrix[y][x]
        while q:
            dis, y, x = heapq.heappop(q)
            if distance[y][x] < dis:
                continue
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0<=ny<n and 0<=nx<n:
                    cost = dis + matrix[ny][nx]
                    if cost < distance[ny][nx]:
                        distance[ny][nx] = cost
                        heapq.heappush(q, (cost, ny, nx))   
        return distance[n-1][n-1]

    print(f'Problem {cnt}:',dijkstra(0, 0))