string = list(input())

result = 0

tmp = 1
stack = []


for i in range(len(string)):
    if string[i] == '(':
        stack.append(string[i])
        tmp *= 2
    if string[i] == '[':
        stack.append(string[i])
        tmp *= 3

    if string[i] == ')':
        if len(stack) == 0 or stack[-1] == '[':
            print(0)
            exit()
        if len(stack) != 0:
            if string[i-1] == '(':
                result += tmp
        stack.pop()
        tmp //= 2

    if string[i] == ']':
        if len(stack) == 0 or stack[-1] == '(':
            print(0)
            exit()
        if len(stack) != 0:
            if string[i-1] == '[':
                result += tmp
        stack.pop()
        tmp = tmp // 3

if stack:
    print(0)
else:
    print(result)