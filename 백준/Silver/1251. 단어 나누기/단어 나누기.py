from itertools import combinations

string = input()
k = len(string)

string_idx = [i for i in range(1,k)]
# 문자열 인덱스 중 3개를 선택하여 모든 조합 구해보기


result = []
for k in combinations(string_idx,2):
    a,b = k[0],k[1]
    r1,r2,r3 = string[:a],string[a:b],string[b:]
    union = r1[::-1]+r2[::-1]+r3[::-1]
    result.append(union)

result.sort()
print(result[0])