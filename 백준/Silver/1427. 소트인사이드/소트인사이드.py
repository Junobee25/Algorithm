number = input()
arr = []
for i in number:
    arr.append(int(i))
arr.sort(reverse=True)
for i in arr:
    print(i,end='')