n, k = map(int,input().split())

tap_list = list(map(int, input().split()))

check_list = []


idx = -1

cnt = 0

## 처음 멀티탭이 꽉찬찬 상황으로 만듦
for i in range(k):
    if len(check_list) < n:
        if tap_list[i] not in check_list:
            check_list.append(tap_list[i])
    else:
        idx = i
        break

for i in range(idx, k):
    if tap_list[i] in check_list:
        continue
    else:
        tap_idx_list = []
        for j in range(len(check_list)):
            if check_list[j] in tap_list[i:]:
                tap_idx_list.append(tap_list[i:].index(check_list[j]))
            else:
                tap_idx_list.append(101)
        target = tap_idx_list.index(max(tap_idx_list))
        check_list.remove(check_list[target])
        check_list.append(tap_list[i])
        cnt += 1

print(cnt)