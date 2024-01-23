n, m = map(int, input().split())
books_info = sorted(list(map(int, input().split())))
visited = [False] * len(books_info)
result = 0

if len(books_info) == 1:
    print(abs(books_info[0]))
    exit()

if abs(books_info[0]) < abs(books_info[-1]):
    result += books_info[-1]
    for i in range(len(visited) - 1, len(visited) - 1 - m, -1):
        if i < 0:
            break
        if books_info[i] < 0:
            break
        visited[i] = True
        
else:
    result += abs(books_info[0])
    for i in range(m):
        if i >= len(books_info):
            break
        if books_info[i] > 0:
            break
        visited[i] = True

start_idx = 0

while True:
    if visited[start_idx]:
        start_idx += 1
        if start_idx >= len(books_info):
            break
        continue

    if books_info[start_idx] < 0:
        result += abs(books_info[start_idx]) * 2
        start_idx += m
        
        
    if start_idx >= len(books_info) or books_info[start_idx] > 0:
        break
   
end_idx = len(books_info) - 1
      
while True:
    if visited[end_idx]:
        end_idx -= 1
        if end_idx < 0:
            break
        continue
    if books_info[end_idx] > 0:
        result += (books_info[end_idx]) * 2
        end_idx -= m
        
    if end_idx < 0 or books_info[end_idx] < 0:
        break
    
print(result) 