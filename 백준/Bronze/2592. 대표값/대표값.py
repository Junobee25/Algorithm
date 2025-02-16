average = 0
mode = 0

dic = {}
for _ in range(10):
    n = int(input())
    average += n

    if n not in dic:
        dic[n] = 1
    else:
        dic[n] += 1


print(average//10)

print(max(dic, key=dic.get))