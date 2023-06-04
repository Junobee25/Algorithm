number = input()

def check_odd(num):
    """
    문자열에 홀수가 몇개 있는지 판단하는 함수
    num => 문자열
    """
    cnt = 0
    for i in num:
        if int(i) % 2 != 0:
            cnt += 1

    return cnt


def one_to_one(num):
    """
    number의 길이가 2가 됬을 때
    숫자 하나 하나 씩 분리하여
    더해주는 함수
    num => 문자열
    """
    return int(num[0]) + int(num[1])


def problem(num,cnt):
    if len(num) == 1:
        result_list.append(cnt) 
        return 
    elif len(num) == 2:
        number = str(one_to_one(num))
        problem(number,cnt+check_odd(number))
    else:
        for i in range(1,len(num)):
            for j in range(i+1,len(num)):
                number = str(int(num[:i]) + int(num[i:j]) + int(num[j:]))
                problem(number,cnt+check_odd(number))
result_list = []
problem(number,check_odd(number))
print(min(result_list),max(result_list))