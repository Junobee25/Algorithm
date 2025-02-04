import sys
N = int(sys.stdin.readline())
x = [[1,1],[1,0]]
def mult(a,b):
    A = [[0,0],[0,0]]
    for i in range(2): 
        for j in range(2):
            for k in range(2):
                A[i][j] += a[i][k] * b[k][j] % 1000000007
                
    return A

def f(x,n):
    if n == 1:
        return x
    else:
        matrix = f(x,n//2)
        if n % 2 == 0:
            return mult(matrix, matrix)
        else:
            return mult(mult(matrix, matrix), x)

result = f(x, N)

print(result[0][1]*result[0][0] % 1000000007)