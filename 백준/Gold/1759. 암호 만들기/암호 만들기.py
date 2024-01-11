target_depth, number_of_alphabet = map(int,input().split())

alphabets = list(map(str,input().split()))
alphabets.sort()
result = []
# a c i s t w
def dfs(current, depth):
    if len(current) == target_depth:
        result.append(current)
        return
        
    for i in range(depth, number_of_alphabet):
        dfs(current + [alphabets[i]], i + 1)
dfs([], 0)

def count_vowel(string):
    vowel_count = 0
    for element in string:
        if element == 'a' or element == 'e' or element == 'i' or element =='o' or element == 'u':
            vowel_count += 1
    return vowel_count

for password in result:
    vowel_cnt = count_vowel(password)
    if vowel_cnt >= 1 and len(password) - vowel_cnt >= 2:
        print(''.join(password))