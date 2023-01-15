N = int(input())
arr = list(map(str,str(input())))
number = []
stack = []
for i in range(N):
    number.append(int(input()))

for x in arr:
    if 'A' <= x <='Z':
        stack.append(number[ord(x)-ord('A')])
    else:
        if x == '+':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2+n1)
        elif x == '-':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2-n1)
        elif x == '*':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2*n1)
        elif x == '/':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2/n1)
print('%.2f'%stack[0])
            