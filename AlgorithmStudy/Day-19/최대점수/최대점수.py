def DFS(L,sum,time):
    global res
    if time > M:
        return # 최근에 호출된 곳으로 돌아감
    if L == N:
        if sum > res:
            res = sum
    else:
        DFS(L+1,sum+arr[L][0],time + arr[L][1])  # 쓴다 -> 가지치기 -> 시간이 오버되면 return 되고 최근에 호출된 다음 줄부터 실행 (재귀함수-Stact자료구조) 
        # ex ) DFS(2,35,17) -> DFS(3,50,25) => return에 걸리고 메모리에서 빠진후 DFS(2,35,17) 다음 줄부터 실행 (3,35,17) -> (4,41,20) -> (5,48,24) => return에 걸리고 DFS(4,41,20) 다음줄
        # DFS(5,41,20) => L = 5 = N , sum=41 > res  print(res) ........ 생각해볼 것 L == N이 되고 res = sum 할당된 이후 함수는 어떻게 동작하는가 재귀호출이 어떻게 끝나는가?,최대값이 다른 값이 될 순 있진
        # 않은가 최댓값이 겹치는 경우는 어떻게 되는가 확실하게 마스터하려면 이부분에 대한 고민이 필요할 듯하다.
        DFS(L+1,sum,time) # 안쓴다 -> 가지치기

N,M = map(int,input().split())
arr = []
for i in range(N):
    k = list(map(int,input().split()))
    arr.append(k)
res = -99999999
DFS(0,0,0)
print(res)