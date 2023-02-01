alpa = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
result = list(input())
for i in range(len(result)):
    if result[i].lower() in alpa:
        if alpa.index(result[i].lower()) < 13:
            if result[i].isupper():
                result[i] = alpa[alpa.index(result[i].lower())+13].upper()
            else:
                result[i] = alpa[alpa.index(result[i])+13]
        else:
            if result[i].isupper():
                result[i] = alpa[alpa.index(result[i].lower())-13].upper()
            else:
                result[i] = alpa[alpa.index(result[i])-13]
for i in range(len(result)):
    print(result[i],end="")

