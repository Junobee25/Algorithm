string = list(input())
string.sort()
# 홀수 개수 2개이상이면 안되고 exit()
count_flag = '0'   
count_list = []
for i in range(len(string)):
    if count_flag != string[i]:
        count_flag = string[i]
        count_list.append(string.count(string[i]))

cnt = 0
for i in count_list:
    if i % 2 != 0:
        cnt += 1
# 좌측 팰린드롬
left = ''
# 중간
half = ''
if cnt >= 2:
    print("I'm Sorry Hansoo")
    exit()
#################################################

# flag = '0'
# result = ['0' for _ in range(len(string))]
# for i in range(len(string)):
#     if flag != string[i]:
#         flag = string[i]
#         print(flag)
#         # 원소의 개수가 짝수면 
#         if string.count(string[i]) % 2 == 0:
#             result[i:i + string.count(string[i])//2] = [string[i] for _ in range(string.count(string[i])//2)]
#             result[len(string)-i-string.count(string[i])//2:len(string)-i] = [string[i] for _ in range(string.count(string[i])//2)]
#         if string.count(string[i]) % 2 != 0 :
#             result[len(result)//2] = string[i]
#             # string.remove(string[i])
#             result[i:i + string.count(string[i])//2] = [string[i] for _ in range(string.count(string[i])//2)]
#             result[len(string)-i-string.count(string[i])//2:len(string)-i] = [string[i] for _ in range(string.count(string[i])//2)]
#     print(result)

# answer = ''
# for i in result:
#     answer += i
# print(string)
# print(answer)
else:
    flag = '0'
    for i in range(len(string)):
        if flag != string[i]:
            flag = string[i]
            # 알파벳이 바뀔 때 마다 left 변수에 알바벳개수//2 를 더해줌 데칼코마디 형태로
            left += string[i]*(string.count(string[i])//2)
    # 홀수일 때 최소 1개 알파벳은 중간에 와야함
    for i in range(len(string)):
        if string.count(string[i]) % 2 != 0:
            half += string[i]
            break
    # 결과 = 좌 + 중간 + 좌(역)
    result = left + half + ''.join(reversed(left))
    print(result)