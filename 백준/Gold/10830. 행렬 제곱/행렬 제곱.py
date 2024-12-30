import sys
input = sys.stdin.readline

a, b = map(int, input().split())

matrix = []

for _ in range(a):
    matrix.append(list(map(int, input().split())))
    

def matrix_multiply(arr1, arr2):
    result = [[0]*a for _ in range(a)]
    for row in range(a):
        for col in range(a):
             s = sum(arr1[row][i] * arr2[i][col] for i in range(a))
             result[row][col] = s % 1000
             
    return result


def power(n, arr):
    if n == 1:
        return arr
    
    if n % 2 == 0:
        half = power(n//2, arr)
        return matrix_multiply(half, half)
    else:
        return matrix_multiply(arr, power(n-1, arr))
        
for row in power(b, matrix):
    print(*[r%1000 for r in row])
        
    