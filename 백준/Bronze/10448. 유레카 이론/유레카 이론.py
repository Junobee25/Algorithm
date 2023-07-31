from itertools import combinations_with_replacement

t = int(input())

tri_arr = []

for i in range(1,46):
    tri_arr.append((i*(i+1))//2)



for _ in range(t):
    k = int(input())
    cnt = 0
    for cr in combinations_with_replacement(tri_arr,3):
        if sum(cr) == k:
            cnt = 1
            break
    print(cnt)