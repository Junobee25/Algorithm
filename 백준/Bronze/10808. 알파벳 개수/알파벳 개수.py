alpa = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
cnt = [0 for i in range(26)]
result = list(input())
for i in result:
    cnt[alpa.index(i)] = result.count(i)
for i in cnt:
    print(i,end=" ")
    