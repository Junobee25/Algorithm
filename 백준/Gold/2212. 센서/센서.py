N = int(input())
K = int(input())

sensor = list(map(int ,input().split()))
sensor.sort()
distance = [sensor[idx] - sensor[idx - 1] for idx in range(1, len(sensor))]
distance.sort()

# N - 1 간선 
# K - 1 제거 할 간선
print(sum(distance[:N-K]))