T = int(input())

stack = []
for i in range(T):
    a = int(input())
    stack.append(a)
    if a == 0:
        stack.pop()
        stack.pop()
print(sum(stack))