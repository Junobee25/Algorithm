from collections import deque

def solution(cacheSize, cities):
    cache = deque([])
    upper_cities = []
     
    for city in cities:
        upper_cities.append(city.upper())

    answer = 0
    for city in upper_cities:
        if (city not in cache):
            answer += 5
            if (len(cache) == cacheSize):
                cache.append(city)
                cache.popleft()
            else:
                cache.append(city)
        else:
            cache.remove(city)
            cache.append(city)
            answer += 1
    return answer