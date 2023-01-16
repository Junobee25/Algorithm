check = input()
cnt = 1
for i in check:
    print(i,end="")
    if cnt == 0:
        pass
    elif cnt%10 == 0:
        print()
    cnt +=1