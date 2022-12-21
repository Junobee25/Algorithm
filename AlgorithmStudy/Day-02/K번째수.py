import sys
input = sys.stdin.readline

T = int(input())
Solution = []
for i in range(T):
    N, s, e, k = map(int,input().split())
    number_List = list(map(int,input().split()))
    new_List = sorted(number_List[s-1:e])       # new_List 보단 number_List로 초기화 하기!
    Solution.append(new_List[k-1])
    

for i in range(T):
    print(Solution[i])
    



 