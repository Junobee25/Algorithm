n = int(input())

a = 0
b = 0
c = 0

for i in range(1, n + 1):
    a += i
    b += i
    c += i**3
    
print(a)
print(b**2)
print(c)