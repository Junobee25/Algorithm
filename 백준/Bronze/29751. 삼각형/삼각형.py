import math

a, b = map(int, input().split())

area = a * b * (1/2)

print(math.floor(area * 10) / 10)