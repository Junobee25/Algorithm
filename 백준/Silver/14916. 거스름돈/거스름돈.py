n = int(input())

result = -1
flag = False
for i in range(n//2 + 1):
    for j in range(n//5 + 1):
        if 2 * i + 5 * j == n:
            result = i + j
            flag = True
            break
        
    if flag:
        break
print(result)
        