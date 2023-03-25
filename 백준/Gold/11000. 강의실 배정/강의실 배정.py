# 문제 이해
# Si에 시작해서 Ti에 끝나는 N개의 수업이 주어지는데, 최소의 강의실을 사용해서 모든 수업을 가능하게 하기

# 접근
# 시작 시간이 빠른 순으로 정렬
# 끝나는 시간보다 시작 시간이 빠르면 힙에 추가
# 끝나는 시간보다 시작 시간이 느리면 힙에서 삭제 후 끝나는 시간 갱신
import heapq

n = int(input())

q = []

for i in range(n):
    q.append(list(map(int,input().split())))

q.sort()

room = []
heapq.heappush(room,q[0][1])

for i in range(1,n):
    if q[i][0] < room[0]:
        heapq.heappush(room,q[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room,q[i][1])
print(len(room))
