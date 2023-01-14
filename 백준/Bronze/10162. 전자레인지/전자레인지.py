time = int(input())
button = [[300,0],[60,0],[10,0]]

while time > 0:
    if time - button[0][0] >= 0:
        time -= button[0][0]
        button[0][1] += 1
    elif time - button[1][0] >= 0:
        time -= button[1][0]
        button[1][1] += 1
    elif time - button[2][0] >= 0:
        time -= button[2][0]
        button[2][1] += 1
    elif time < 10:
        break




if int(str(time)[-1]) != 0 :
    print(-1)
else:
    for i in button:
        print(i[1],end=" ")
