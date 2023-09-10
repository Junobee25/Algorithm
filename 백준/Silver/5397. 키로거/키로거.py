t = int(input())
import sys
from collections import deque
input = sys.stdin.readline

for _ in range(t):
    string = input().rstrip()
    password = []
    arr = []
    arr = deque(arr)
    temp_idx = 0
    for i in range(len(string)):
        # 문자일 때만 password배열에 append
        if string[i] != '<' and string[i] != '>' and string[i] != '-':
            password.append(string[i])
        # 문자가 아님 ==> '<'
        if string[i] == '<':
            if len(password) != 0:
                word = password.pop()
                arr.appendleft(word)
        if string[i] == '>':
            if len(arr) != 0:
                word_2 = arr.popleft()
                password.append(word_2)
        if string[i] == '-':
            if len(password) != 0:
                password.pop()

    arr = list(arr)
    result_arr = password + arr
    for k in result_arr:
        print(k, end =  "")
    print()
            