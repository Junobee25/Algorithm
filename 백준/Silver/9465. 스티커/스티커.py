# for i in range(T):
#     dp = []
#     dp2 = []
#     N = int(input().rstrip())
#     one = list(map(int,input().split()))
#     two = list(map(int,input().split()))
#     one.insert(N-1,0)
#     one.insert(N,0)
#     two.insert(N-1,0)
#     two.insert(N,0)
#     if N == 1:
#         dp.append(max(one[0],two[0]))
#         print(dp[0])
#     elif N == 2:
#         dp.append(max(one[0]+two[1],one[1]+two[0]))
#         print(dp[0])
#     else:
#         for j in range(int((N-1)/2+1)):
#             if one[2*j+2]+two[2*j+1]<=two[2*j+1]:
#                 dp.append(one[2*j]+two[2*j+2])
#             else:
#                 dp.append(one[2*j]+two[2*j+1])
#         for k in range(int((N-1)/2+1)):
#             if two[2*k+1]+one[2*k]<=one[2*k+1]:
#                 dp2.append(two[2*k]+one[2*k+2])
#             else:
#                 dp2.append(two[2*k]+one[2*k+1])
#         print(max(sum(dp),sum(dp2)))
import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    dp = [list(map(int,input().split())) for _ in range(2)]

    if N > 1:
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]
    for i in range(2,N):
        dp[0][i] += max(dp[1][i-1],dp[1][i-2])
        dp[1][i] += max(dp[0][i-1],dp[0][i-2])
    
    print(max(dp[0][N-1],dp[1][N-1]))



