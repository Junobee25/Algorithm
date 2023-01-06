N = int(input())

home = 1
cnt = 1
while N > home :
    home += 6 * cnt
    cnt += 1
print(cnt)