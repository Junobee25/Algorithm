A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())
result = 0
if P<=C:
    result = B
else:
    result = B +(P-C)*D
print(min(A*P,result))