import sys
input = sys.stdin.readline

n = int(input())
S = []
for _ in range(n):
    cmd_list = list(input().rstrip().split())
    if cmd_list[0] == "add":
        if int(cmd_list[1]) in S:
            pass
        else:
            S.append(int(cmd_list[1]))
    if cmd_list[0] == "remove":
        if int(cmd_list[1]) not in S:
            pass
        else:
            S.remove(int(cmd_list[1]))
    if cmd_list[0] == "check":
        if int(cmd_list[1]) in S:
            print(1)
        else:
            print(0)
    if cmd_list[0] == "toggle":
        if int(cmd_list[1]) in S:
            S.remove(int(cmd_list[1]))
        else:
            S.append(int(cmd_list[1]))
    if cmd_list[0] == "all":
        S = [i for i in range(1,21)]
    
    if cmd_list[0] == "empty":
        S = []

