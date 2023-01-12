N = int(input())
time_case = list(map(int,input().split()))
time = 0
time_case.sort()
for i in range(N):
    time += sum(time_case[:i+1])
print(time)    