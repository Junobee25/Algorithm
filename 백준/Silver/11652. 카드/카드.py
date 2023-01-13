import sys
input = sys.stdin.readline

N = int(input())


hash = {}
for i in range(N):
    cnt = int(input())
    if cnt not in hash:
        hash[cnt] = 1
    else:
        hash[cnt] += 1
result = sorted(hash.items(),key = lambda x: (-x[1],x[0]))

print(result[0][0])