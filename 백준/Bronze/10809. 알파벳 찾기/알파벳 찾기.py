str1 = input()
alpa = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for j in range(0,len(alpa)):
    if alpa[j] in str1:
        print(str1.index(alpa[j]),end= " ")
    else:
        print(-1,end=" ")
