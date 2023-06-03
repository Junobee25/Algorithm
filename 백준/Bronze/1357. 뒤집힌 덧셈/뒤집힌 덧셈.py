
num1,num2 = input().split()

def rev(num):
    """
    num => str 을 받고
    뒤집힌 num(int형)을 return
    """
    num = num[::-1]
    new_num = ''
    check = False
    for i in num:
        if int(i) != 0:
            check = True
        if check == True:
            new_num += i
    return int(new_num)

print(rev(str(rev(num1) + rev(num2))))