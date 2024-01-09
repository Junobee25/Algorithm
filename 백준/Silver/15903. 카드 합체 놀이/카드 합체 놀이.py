import heapq

n, m = map(int,input().split())
cards = list(map(int,input().split()))

min_heap = []

for card in cards:
    heapq.heappush(min_heap, card)
    
for i in range(m):
    a = heapq.heappop(min_heap)
    b = heapq.heappop(min_heap)
    
    k = a + b
    
    heapq.heappush(min_heap, k)
    heapq.heappush(min_heap, k)
    
print(sum(min_heap))