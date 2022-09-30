a = int(input())
num = a
for i in range(a):
    word = input()
    for j in range(0,len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            num -= 1
            break
        

print(num)