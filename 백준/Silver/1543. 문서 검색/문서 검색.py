a = input()
b = input()

check_a = [False] * len(a)
result_cnt = 0
# 앞에서 부터 문자열 판단
for i in range(len(a)-len(b)+1):
    if check_a[i] == False:
        if a[i:i+len(b)] == b:
            for j in range(i,i+len(b)):
                check_a[j] = True
            result_cnt += 1
print(result_cnt)
