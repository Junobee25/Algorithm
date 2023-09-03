import sys
input = sys.stdin.readline

while True:
    # [S,d]
    string = list(input().rstrip())
    lenn = len(string)
    stack = []
    if string[0] == '.':
        break
    flag = True
    for i in range(lenn):
        if string[i] == '[' or string[i] == '(':
            stack.append(string[i])
        
        if len(stack) == 0 and (string[i] == ']' or string[i] == ')'):
            print('no')
            flag = False
            break

        if string[i] == ']' and stack[-1] == '[':
            stack.pop()
        elif string[i] == ']' and stack[-1] == '(':
            print('no')
            flag = False
            break
        if string[i] == ')' and stack[-1] == '(':
            stack.pop()

        elif string[i] == ')' and stack[-1] == '[':
            print('no')
            flag = False
            break
    if len(stack) == 0 and flag:
        print('yes')
    
    if len(stack) != 0 and flag:
        print('no')