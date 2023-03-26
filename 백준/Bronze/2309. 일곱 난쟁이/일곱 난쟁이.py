from itertools import combinations

arr = []

for i in range(9):
    arr.append(int(input()))
    
for i in combinations(arr,7):
    if sum(i) == 100:
        i = list(i)
        i.sort()
        for j in i:
            print(j)
        break