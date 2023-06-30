# 현재 시점을 기준으로 양 옆에 작은 블록이 있다면 쌓일 수 없음

# 빗물이 채워질려면 양 옆의 블록이 모두 높아야 함

height,width = map(int,input().split())

world = list(map(int,input().split()))

result = 0

for i in range(1,width-1):
    lm = max(world[:i])
    rm = max(world[i+1:])
    
    compare = min(lm,rm)
    
    if world[i] < compare:
        result += compare - world[i]
        
print(result)