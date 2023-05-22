# 집합자료형에 담아서 갯수 체크

# 키들을 정렬

n = int(input())

fileset = {}

for i in range(n):
    filename = input().split('.')
    if filename[1] not in fileset:
        fileset[filename[1]] = 1
    else:
        fileset[filename[1]] += 1

result = []
for i in fileset.items():
    result.append(i)

result.sort()

for i,j in result:
    print(i,j)