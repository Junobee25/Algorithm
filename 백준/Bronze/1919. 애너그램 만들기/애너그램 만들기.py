# 겹치는 문자 다 찾기
a = input()
b = input()

check_a = [False]*len(a)
check_b = [False]*len(b)
for i in range(len(a)):
    for j in range(len(b)):
        if check_b[j] == False:
            if a[i] in b[j]:
                check_b[j] = True
                check_a[i] = True
                break

print(check_b.count(False)+check_a.count(False))