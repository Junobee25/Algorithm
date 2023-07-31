n = int(input())
number_set = set(list(map(int,input().split())))
result_num = int(input())
cnt = 0
for i in number_set:
    k = result_num - i
    if k in number_set:
        cnt += 1

print(cnt//2)