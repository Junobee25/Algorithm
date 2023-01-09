N = int(input())
arr1 = list(map(int,input().split()))
M = int(input())
arr2 = list(map(int,input().split()))
arr1.sort()

for i in arr2:
    lt = 0  
    rt = len(arr1) - 1
    isExist = False
    while lt <= rt:
        mid = (lt+rt)//2
        if arr1[mid] == i:
            isExist = True
            print(1)
            break
        elif arr1[mid] <= i:
            lt = mid + 1
        elif arr1[mid] > i:
            rt = mid - 1
    if not isExist:
        print(0)