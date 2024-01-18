import sys
input = sys.stdin.readline
test_case = int(input())

for _ in range(test_case):
    N = int(input())
    result = 1
    score_info = []
    
    for _ in range(N):
        score_info.append(list(map(int, input().split())))
        
    score_info.sort(key = lambda x : x[0])
    rank = score_info[0][1]

    for i in range(1, N):
        if score_info[i][1] < rank:
            result += 1
            rank = score_info[i][1]    
            
    print(result)