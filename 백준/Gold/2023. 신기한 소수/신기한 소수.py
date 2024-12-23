
n = int(input())


def check_deci(check_num):
    for i in range(2, int(check_num**0.5) + 1):
        if int(check_num)%i == 0:
            return False
    return True


def dfs(num):
    if len(str(num)) == n:
        print(num)
    else:
        for i in range(10):
            temp = 10 * num + i

        
            if check_deci(temp):
                dfs(temp)
dfs(2)
dfs(3)
dfs(5)
dfs(7)