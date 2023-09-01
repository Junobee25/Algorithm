import sys

input = sys.stdin.readline

T = int(input())
def isPal(s,left,right):
    while (left <= right):
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


for _ in range(T):
    string = input().rstrip()    
    if string == string[::-1]:
        print(0)
    else:
        flag = False
        for i in range(len(string)//2):
            if string[i] != string[len(string)-i-1]:
                if isPal(string,i,len(string)-i-2) or isPal(string,i+1,len(string)-i-1):
                    flag = True
                break

        if flag:
            print(1)
        else:
            print(2)