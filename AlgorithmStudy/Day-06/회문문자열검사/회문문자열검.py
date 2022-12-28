import sys
input = sys.stdin.readline
N = int(input())

# Test = []
# ReverseTest = []
# for i in range(N):
#     Test.append(list(input().lower()))
#     ReverseTest.append(Test[i])
#     ReverseTest[i].reverse() >> Test[i]를 바꿔버림
# for i in range(N):
#     if Test[i] == ReverseTest[i] :
#         print(Test[i]," ",ReverseTest[i])
#         print("YES")
#     elif Test[i] != ReverseTest[i] :
#         print("NO")

for i in range(N):
    # sys는 개행문자포함이니 공백제거 해줘야함
    s = input().rstrip()
    s = s.upper()
    print(s[::-1])
    if s == s[::-1]:
        print("YES")
    else:
        print("NO")