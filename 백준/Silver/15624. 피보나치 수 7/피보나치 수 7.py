n = int(input())

matrix = [[1,1],[1,0]]

def mult_matrix(a,b):
    arr = [[0,0],[0,0]]
    for k in range(2):
        for i in range(2):
            for j in range(2):
                arr[i][j] += a[i][k]*b[k][j]
                arr[i][j] %= 1000000007
    return arr


def mult(n,matrix):
    if n == 1:
        return matrix
    temp = mult(n//2, matrix)
    if n % 2:
        return mult_matrix(matrix, mult_matrix(temp, temp))
    else:
        return mult_matrix(temp, temp)    
    
if n == 0:
    print(0)
else:
    print(mult(n, matrix)[0][1])