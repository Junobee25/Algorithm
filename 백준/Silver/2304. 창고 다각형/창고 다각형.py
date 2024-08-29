n = int(input())

arr = []

for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a,b))

arr.sort()
    
max_height = 0
index = 0

for i in range(n):
    if arr[i][1] > max_height:
        max_height = arr[i][1]
        index = i
        
s_x = arr[0][0]
s_y = arr[0][1]
left_extent = 0

for i in range(0, index + 1):
    if arr[i][1] >= s_y:
        left_extent += s_y * (arr[i][0] - s_x)
        s_x = arr[i][0]
        s_y = arr[i][1]
        

e_x = arr[-1][0]
e_y = arr[-1][1]
right_extent = 0

for i in range(n - 1, index - 1, -1):
    if arr[i][1] >= e_y:
        right_extent += e_y * abs(arr[i][0] - e_x)
        e_x = arr[i][0]
        e_y = arr[i][1]

print(left_extent + right_extent + arr[index][1])