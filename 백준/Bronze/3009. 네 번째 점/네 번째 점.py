co_x = []
co_y = []

for i in range(3):
    x,y = map(int,input().split())
    co_x.append(x)
    co_y.append(y)

for i in co_x:
    if co_x.count(i) == 1:
        print(i,end=" ")
for j in co_y:
    if co_y.count(j) == 1:
        print(j)