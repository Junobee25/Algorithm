
n = int(input())
star = ['***','* *','***']
if n == 3:
    for i in star:
        print(i)
    exit()


value = [0]*7
value[0] = 3
for i in range(1,7):
    value[i] = value[i-1]*3




for k in range(9,n+1):
    temp = []
    if k in value:
        for i in range(k):
            if 1 <= i // (k//3) < 2 :
                temp.append(star[i%(k//3)] + ' ' * (k // 3) + star[i%(k//3)])
            else:
                temp.append(star[i%(k//3)]*3)

    
        star = temp

for i in star:
    print(i)