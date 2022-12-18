# 리스트와내장함수
import random as r
a = []   # 빈리스트 만들기
print(a)
b = list()  # 빈리스트 만들기
print(b)
b = list(range(1, 11))  # 1 ~ 10 까지 리스트 만들기

b.append(9)  # b 리스트에 9 추가
b.insert(3, 7)  # b 리스트 3인덱스에 7 삽입
b.pop()  # 맨 뒷자리 원소 리스트에서 제거
b.pop(3)  # 3번 인덱스 제거하기
b.remove(4)  # b 리스트에서 4 원소제거하기
b.index(5)  # b리스트의 5라는 값의 index번호를 리턴 (처음 나오는 5)
print(sum(b))  # b리스트의 원소의 총합
print(max(b))  # b리스트 원소중에 최대값
print(min(b))  # b리스트 원소중에 최소값
print(min(7, 5))  # 인자값들 중에서 최소값 찾아줌
r.shuffle(b)  # b리스트 원소들을 무작위로 섞어라
b.sort()  # b리스트 원소를 오름차순으로 정렬하라
b.sort(reverse=True)  # b리스트 원소를 내림차순으로 정렬하라
b.clear()  # b리스트를 빈리스트로 만듦
