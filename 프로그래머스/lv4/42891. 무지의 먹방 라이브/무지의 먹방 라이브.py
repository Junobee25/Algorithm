# 링크 https://www.youtube.com/watch?v=zpz8SMzwiHM

from operator import itemgetter

def solution(food_times, k):   
    foods = []
    n = len(food_times)
    for i in range(n):
        foods.append((food_times[i], i + 1))
    foods.sort()
    s = 0
    for i, food in enumerate(foods):
        diff = food[0] -s
        if diff != 0:
            spend = diff * n
            if spend <= k :
                k -= spend
                s = food[0]
            else:
                k %= n
                # sublist = sorted(foods[i:], key = itemgetter(1))
                sublist = sorted(foods[i:], key = lambda x : x[1])
                return sublist[k][1]
        n -= 1 
    return -1

# 배운 점
# 1초가 지났을 때 남아있는 음식을 하나하나 확인하는 것이 아니라
# 1초가 지났을 때 먹을 수 있는 음식을 한번에 처리해 줌으로써 diff * n
# 시간복잡도를 줄일 수 있음
# k초가 지난 후 남아있는 음식들 중에서 나머지를 통해 인덱스를 구하고
# itemgetter 메소드로 정렬 후 return
