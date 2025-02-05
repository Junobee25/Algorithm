n, m = map(int, input().split())

x = [[1,1],[1,0]]

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
    
def matrix_mult(a, b):
    A = [[0,0],[0,0]]
    
    for k in range(2):
        for i in range(2):
            for j in range(2):
                A[i][j] += a[i][k]*b[k][j] % 1000000007
                
    return A

def f(x,n):
    if n == 1:
        return x
    else:
        matrix = f(x, n//2)
        if n % 2 == 0:
            return matrix_mult(matrix, matrix)
        else:
            return matrix_mult(matrix_mult(matrix,matrix), x)
        
resultN = f(x,n)
resultM = f(x,m)



print(f(x,gcd(n,m))[0][1]%1000000007)

