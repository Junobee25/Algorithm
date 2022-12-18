# 리스트와 내장함수(2)
a = [23, 12, 36, 53, 19]
print(a[:3])
print(a[1:4])
print(len(a))
# 원소와 인덱스번호까지 가져오고 싶을 때 이너머레이트 (0,23) 튜플형으로 리턴
for x in enumerate(a):
    print(x)
# 튜플 (값을 변경할 수 없음)
b = (1,2,3,4,5)
print(b[0])
b[0] = 7 # Error
# enumerate 로 많이 사용하는 형태
for index,value in enumerate(x):
    print(index,value)
# all 함수
if all(x >60 for x in a): # all 괄호 안에 루트가 모두 참이면 True 리턴 하나라도 거짓이면 False
    print('Yes')
else:
    print('No')
# any 함수
if any(15>x for x in a): # any 괄호 안에 루트가 하나라도 참이면 True 모두다 거짓이면 False
    print('Yes')
else:
    print('No')