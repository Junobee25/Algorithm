# N*M크기의 직사각형에서 꼭짓점의 수가 같은 제일 큰 정사각형의 크기를 구하는 문제

# 접근
# N*M 크기 내 요소 하나하나에 대해 만들어질 수 있는 정사각형을 찾은 다음
# 기준 값보다 크다면 max_val을 갱신(크기)

n,m = map(int,input().split())

squared = []

for _ in range(n):
    squared.append(list(input()))
max_val = 1
for i in range(n):
    for j in range(m):
        # 행과 열의 개수중 작은 값까지 정사각형을 만들 수 있음
        for k in range(1,min(n,m)+1):
            # 정사각형을 행렬 내부에 있고
            if 0 < j + k < m and 0 < i + k < n:
                # 꼭짓점의 수가 같을 때
                if squared[i][j] == squared[i][j+k] == squared[i+k][j] == squared[i+k][j+k]:
                    if k + 1 > max_val:
                        max_val = k + 1

print(max_val**2)