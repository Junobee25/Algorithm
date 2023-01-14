while True:
    arr = list(map(int,input().split()))
    if arr == [0,0,0]:
        break
    bin = max(arr)**2
    arr.pop(arr.index(max(arr)))
    result = 0
    for i in arr:
        result += i**2
    if bin != result:
        print('wrong')
    else:
        print('right')
