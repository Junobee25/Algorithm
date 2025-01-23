result = 0
result2 = ''
for i in range(3):
    k = int(input())
    if i == 0:
        result += k
        result2 = result2 + str(k)
    elif i == 1:
        result += k
        result2 = result2 + str(k)
    else:
        result -= k
        result2 = int(result2) 
        result2 -= k

print(result)
print(result2)