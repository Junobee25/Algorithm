n = int(input())
cow_info = {}

cnt = 0
for _ in range(n):
    a,b = map(int,input().split())
    if a not in cow_info:
        cow_info[a] = b
        continue
    elif a in cow_info.keys():
        if cow_info[a] != b:
            cow_info[a] = b
            cnt += 1

print(cnt)
