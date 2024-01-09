N = int(input())

top = list(map(int, input().split()))
top = [0] + top
point_info = [0] * (len(top))
stack = []

for i in range(1, N + 1):
    while stack and top[stack[-1]] < top[i]:
        stack.pop()
    point_info[i] = stack[-1] if stack else 0
    stack.append(i)

point_info = point_info[1:]
print(' '.join(map(str, point_info)))