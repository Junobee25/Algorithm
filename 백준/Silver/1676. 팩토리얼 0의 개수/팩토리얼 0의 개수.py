N = int(input())
number = 1
for i in range(1,N+1):
    number*=i
new_number = str(number)
cnt = 0
for i in range(1,len(new_number)+1):
    if new_number[-i] == '0':
        cnt += 1
    else:
        break
print(cnt)
        
    