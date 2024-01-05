import sys
N, M = map(int, input().split(" "))

data = {}

for i in range(N):
    url, password = sys.stdin.readline().rstrip().split(" ")
    data[url] = password


for j in range(M):
    url = sys.stdin.readline().rstrip()
    print(data[url])