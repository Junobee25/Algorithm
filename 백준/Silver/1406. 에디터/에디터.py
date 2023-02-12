# import sys
# input = sys.stdin.readline
# arr = list(map(str,input().rstrip()))
# N = int(input().rstrip())
# cmd = []
# point = len(arr)
# zz = 0
# for i in range(N):
#     choice = list(input().split())
#     cmd.append(choice)
# for i in range(N):
#     if cmd[i][0] == 'P':
#         arr = arr[0:point] +list(cmd[i][1]) + arr[point:]
#         point+=1
#     elif cmd[i][0] == 'L':
#         if point == 0:
#             pass
#         else:
#             point -= 1
#     elif cmd[i][0] == 'D':
#         if point == len(arr):
#             pass
#         else:
#             point += 1
#     elif cmd[i][0] == 'B':
#         if point == 0:
#             pass
#         else:
#             arr.pop(point-1)
#             point -= 1
# for i in arr:
#     print(i,end="")
# 시간초과
# import sys
# input = sys.stdin.readline
# arr = list(input())
# cmd = []
# N = int(input().rstrip())
# point = len(arr)
# for i in range(N):
#     choice = list(input().split())
#     if choice[0] == "P":
#         arr.append(choice[1])
#     if choice[0] == "L":
#         if arr != []:
#             cmd.append(arr.pop())
#     if choice[0] =="D":
#         if(cmd != []):
#             arr.append(cmd.pop())
#     if choice[0] == "B":
#         if(arr):
#             arr.pop()
# print("".join(arr),end="")
# print("".join(list(reversed(cmd))),end="")

import sys
arr = list(input())
N = int(input())
cmd = []

point = len(arr)
for i in range(N):
    choice = sys.stdin.readline().split()

    if(choice[0] == 'L'):
        if(arr != []):
            cmd.append(arr.pop())

    if(choice[0] == 'D'):
        if(cmd != []):
            arr.append(cmd.pop())

    if(choice[0] == 'B'):
        if(arr):
            arr.pop()

    if(choice[0] == 'P'):
        arr.append(choice[1])

print(''.join(arr),end='')
print(''.join(list(reversed(cmd))),end='')