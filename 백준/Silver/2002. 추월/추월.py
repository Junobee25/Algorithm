import sys
input = sys.stdin.readline
N = int(input())

in_info = {}
out_info = {}
cnt = 0
for i in range(2*N):
    if i < N:
        in_car = input().rstrip()
        in_info[in_car] = i
    else:
        out_car = input().rstrip()
        out_info[out_car] = i
        
for k, v in out_info.items():
    for k2, v2 in in_info.items():
        if v2 < in_info[k]:
            if out_info[k2] > v:
                cnt += 1
                break
print(cnt)     