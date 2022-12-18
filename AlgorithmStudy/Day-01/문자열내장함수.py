# 문자열과 내장함수
msg = "It is Time"
print(msg.upper())  # 대문자화
print(msg)         # msg는 그대로
print(msg.lower())  # 소문자화
tmp = msg.upper()
print(tmp)
print(tmp.find('T'))  # 처음 등장하는 T의 Index 번호 리턴
print(tmp.count('T'))  # 문자열에 포함된 T의 갯수 리턴
print(msg[:2])  # 0~1 까지 출력
print(msg[3:5])  # 3~4 까지 출력
print(len(msg))

# 문자열에서 대문자만 출력하기
for x in msg:
    if x.isupper():  # x가 대문자일때 True 리턴
        print(x, end=" ")
print()
# 문자열에서 소문자만 출력하기
for x in msg:
    if x.islower():  # x가 소문자일때 True 리턴
        print(x, end=" ")
print()
# 문자열에서 알파벳일때만 출력하기
for x in msg:
    if x.isalpha():  # x가 알파벳일때 True 리턴
        print(x, end="")
print()
# 아스키넘버 출력하기  A(65) ~ Z(90)
tmp = "AZ"
for x in tmp:
    print(ord(X))
# 아스키넘버 출력하기 a(97) ~ z(122)
tmp = "az"
for x in tmp:
    print(ord(x))
# 아스키넘버라고 생각했을때 65라는 숫자가 문자로는 뭐냐
tmp = 65
print(chr(tmp))
