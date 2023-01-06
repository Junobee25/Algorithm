arr =[]
work = [t for t in range(1,31)]
solution = []
for i in range(28):
    arr.append(int(input()))

for j in work:
    if j not in arr:
        solution.append(j)
if solution[0] > solution[1]:
    solution[0],solution[1] = solution[1],solution[0]
for k in solution:
    print(k)