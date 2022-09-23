num = int(input())
n = 0
list1 = []
while(n<num):
    
    re,ov =input().split(' ')
    re = int(re)

    new_ov = ''
    for i in range(len(ov)):
        new_ov += ov[i]*re
    list1.append(new_ov)
    n+=1
for i in range(len(list1)):
    print(list1[i])
    