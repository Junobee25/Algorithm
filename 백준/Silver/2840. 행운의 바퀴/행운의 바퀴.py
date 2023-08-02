n,k = map(int,input().split()) # n은 바퀴의 수 == 행렬 길이, k는 회전 수

arr = ['?' for _ in range(n)]
# 회전이니 인덱스는 누적합의 나머지로 할당
tmp = 0
for _ in range(k):
    idx,data = input().split()
    idx = int(idx)
    tmp += idx
    if arr[tmp%n] == '?':
        arr[tmp%n] = data
    elif arr[tmp%n] == data:
        continue
    elif arr[tmp%n] != data:
        print('!')
        exit()
alpa_dict = {}
for i in arr:
    if i not in alpa_dict:
        alpa_dict[i] = 1
    else:
        alpa_dict[i] += 1

for k,v in alpa_dict.items():
    if k != '?' and v > 1:
        print('!')
        exit()

for i in range(n,0,-1):
    print(arr[(i + tmp%n)%n], end ="")



