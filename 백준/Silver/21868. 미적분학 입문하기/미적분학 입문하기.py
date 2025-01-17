numerator, denominator = map(int, input().split())
coefficient, constant = map(int, input().split())
x0 = int(input())

limit = coefficient * x0 + constant

print(limit)

if coefficient == 0:
    print('0 0')
else:
    result1 = int(numerator)
    result2 = int(denominator) * abs(coefficient)
    print(result1, result2)
