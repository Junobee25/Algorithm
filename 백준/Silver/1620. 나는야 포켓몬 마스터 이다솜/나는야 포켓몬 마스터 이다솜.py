# import sys
# input = sys.stdin.readline
# # 포켓몬의 갯수 맞춰야하는 갯수
# N,M = map(int,input().split())

# ## 리스트 인덱스와 이름을 담기
# poketmon = []  ##[피카츄,라이츄,꼬부기,,,,,,,,]
# for i in range(N):
#     poketmon.append(input().rstrip())
# for j in range(M):
#     t = input().rstrip()
#     if t.isdecimal():
#         t = int(t)
#         print(poketmon[t-1])
#     elif t in poketmon:
#         print(poketmon.index(t)+1)
# print(poketmon)

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
dogam = []
hash = {}
# hash 자료형에 삽입 {포켓몬이름:번호} key value 형식
for i in range(1,N+1):
    poketmon = input().rstrip()
    dogam.append(poketmon)
    if poketmon not in hash:
        hash[poketmon] = i    # key str  value int

result = [input().rstrip() for _ in range(M)]
for p in result:
    if p.isdecimal():
        print(dogam[int(p)-1])
    else:
        print(hash[p])
