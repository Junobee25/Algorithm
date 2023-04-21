n = int(input())
a = [4]
s = 2
b = 1
sum = 0
for i in range(1, 16):
    s += b
    sum = s ** 2
    a.append(sum)
    b = b * 2
print(a[n])