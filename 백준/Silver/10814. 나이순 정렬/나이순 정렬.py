T = int(input())
arr = []
for i in range(T):
    age,name = input().split()
    age = int(age)
    arr.append([age,name])
arr.sort(key=lambda x : (x[0]))
for i in arr:
    print(i[0],i[1])

