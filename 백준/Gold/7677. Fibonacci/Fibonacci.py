def mult(a,b):
    arr = [[0,0], [0,0]]
    for k in range(2):
        for i in range(2):
            for j in range(2):
                arr[i][j] += a[i][k]*b[k][j] % 10000
    return arr


# 행렬을 n번 곱했을 때의 피보나치 수열 구하기
def f(x,n):
    if n == 1:
        return x
    else:
        matrix = f(x, n//2)
        if n % 2 == 0:
            return mult(matrix, matrix)
        else:
            return mult(mult(matrix, matrix), x)
        
import sys
input = sys.stdin.readline
while True:
    n = int(input())
    if n == -1:
        break
    elif n == 0:
        print(0)
    else:
        x = [[1,1],[1,0]]
        result = f(x,n)
        print(result[0][1] % 10000)