a, r, n, m = map(int, input().split())

def matrix_mul(a,b):
    A = [[0,0],[0,0]]
    for k in range(2):
        for i in range(2):
            for j in range(2):
                temp = (a[i][k]*b[k][j]) % m
                A[i][j] = (A[i][j] + temp) % m

    return A


def f(a,n):
    if n == 1:
        return a
    else:
        temp = f(a, n//2)

        if n % 2 == 0:
            return matrix_mul(temp, temp) 
        else:
            return matrix_mul(matrix_mul(temp, temp), a)


matrix = [[r,0],[a,1]]

result = f(matrix, n)
print(result[1][0] % m)