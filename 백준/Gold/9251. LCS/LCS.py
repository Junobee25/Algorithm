from copy import deepcopy

A = input()
B = input()




min_len = min(len(A),len(B))
max_len = max(len(A),len(B))
matrix = [[0]*(max_len+1) for _ in range(min_len+1)]

for i in range(1,min_len+1):
    for j in range(1,max_len+1):
        # A가 더 짧은 길이 문자열 이면
        if len(A) <= len(B):
            if A[i-1] == B[j-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1

            else:
                matrix[i][j] = max(matrix[i][j-1],matrix[i-1][j])
        else:
            if A[j-1] == B[i-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1

            else:
                matrix[i][j] = max(matrix[i][j-1],matrix[i-1][j])


print(matrix[-1][-1])