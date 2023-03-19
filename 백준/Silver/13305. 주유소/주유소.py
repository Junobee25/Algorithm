# 도시의 개수 100,000개 O(N^2)으로는 풀 수 없네
# O(N)으로 풀어보자
# 문제 이해
# 노드마다 곱의 가중치가 있고,
# 다음 노드로 가는 거리가 주어져 있음
# 다음 노드로 가는 비용은 거리 * 가중치
# 최종 목적지까지의 최소 비용을 구하는 문제

# 접근
# 1. 시작 노드부터 거치는 노드 마다 도착지까지의 거리가 얼마나 남았는지 체크
# 2. 노드마다 가중치에 거리를 얼마나 곱해야하는지 최대 값부터 탐색
# 3. check point(노드) 도달 할 수있다면 최솟값을 갱신 갈수 없다면 break
# 4. 도착 노드부터 check point(노드) 도달 할 수있다면 최솟값 갱신
# 3. 남아있는 거리가 가중치곱의 배수가 아니라면 패스
# 배수라면 1,2,3,4 과정 반복

# 최소비용인 주유소에서 다 넣어버리기

n = int(input())
distance = list(map(int,input().split()))
cost = list(map(int,input().split()))
new_cost = cost[:len(cost)-1]
check = min(new_cost)
re_dist = sum(distance)

result = 0
for i in range(len(distance)):
    if cost[i] != check:
        result += distance[i]*cost[i]
        re_dist -= distance[i]
    else:
        result += re_dist * check
        break
print(result)
    
    
    



  