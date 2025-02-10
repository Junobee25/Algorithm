def matrix_mul(a, b, m):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] = (result[i][j] + a[i][k] * b[k][j]) % m
    return result

def matrix_power_modular(a, n, m):
    result = [[1, 0], [0, 1]]  # Identity matrix
    while n > 0:
        if n % 2 == 1:
            result = matrix_mul(result, a, m)
        a = matrix_mul(a, a, m)
        n //= 2
    return result

a, r, n, mod = map(int, input().split())

base_matrix = [[r, 0], [a, 1]]

result_matrix = matrix_power_modular(base_matrix, n, mod)

print(result_matrix[1][0])