arr = ['a','e','i','o','u']
arr2 = ['A','E','I','O','U']

while True:
    answer = input()
    cnt = 0
    if answer == "#":
        break
    for i in answer:
        if i in arr:
            cnt += 1
        if i in arr2:
            cnt += 1
    print(cnt)

