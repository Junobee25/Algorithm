n = int(input())

def matrixmult(a,b):
    arr = [[0 for _ in range(8)] for _ in range(8)]

    for t in range(8):
        for i in range(8):
            for j in range(8):
                arr[i][j] += (a[i][t] * b[t][j])
                arr[i][j] %= 1000000007
    return arr

def multiply(a,n):
    if n == 1:
        return a
    temp = multiply(a, n//2)
    if n % 2 == 1:
        return matrixmult(a, matrixmult(temp, temp))
    else:
        return matrixmult(temp, temp)

matrix = [[0, 1, 1, 0, 0, 0, 0, 0],
          [1, 0, 1, 1, 0, 0, 0, 0],
          [1, 1, 0, 1, 1, 0, 0, 0],
          [0, 1, 1, 0, 1, 1, 0, 0],
          [0, 0, 1, 1, 0, 1, 0, 1],
          [0, 0, 0, 1, 1, 0, 1, 0],
          [0, 0, 0, 0, 0, 1, 0, 1],
          [0, 0, 0, 0, 1, 0, 1, 0]]


if n == 1:
    print(0)
else:
    k = multiply(matrix,n)
    print(k[0][0])