from collections import deque

def solution(cacheSize, cities):
    cache = deque([])

    answer = 0
    for city in cities:
        new_city = city.upper()
        if (new_city not in cache):
            answer += 5
            if (len(cache) == cacheSize):
                cache.append(new_city)
                cache.popleft()
            else:
                cache.append(new_city)
        else:
            cache.remove(new_city)
            cache.append(new_city)
            answer += 1
            
    return answer