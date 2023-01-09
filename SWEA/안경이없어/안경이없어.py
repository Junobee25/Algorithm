T = int(input())
A = ['C','E','F','G','H','I','J','K','L','M','N','S','T','U','V','W','X','Y','Z'] 
B = ['A','D','O','P','Q','R']
for i in range(T):
    str1,str2 = input().split()
    arr1 = []
    arr2 = []
    for x in str1:
        arr1.append(x)
    for y in str2:
        arr2.append(y)

    for z in range(len(arr1)):  # 구멍없는 문자리스트에 포함 = 1
        if arr1[z] not in A:
            arr1[z] = 1
        else:
            arr1[z] = 0
    for k in range(len(arr2)):  # 구멍있는 문자리스트에 포함 = 0
        if arr2[k] not in A:
            arr2[k] = 1
        else:
            arr2[k] = 0
    if arr1 != arr2:  # 다르면 같으면 결과 출력
        print("#"+str(i+1)+' '+'DIFF')
    else:
        print("#"+str(i+1)+' '+'SAME')