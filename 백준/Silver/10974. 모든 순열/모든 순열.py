from itertools import permutations

n = int(input())
arr = [i for i in range(1, n + 1)]

for sub_list in permutations(arr, len(arr)):
    
    test = ' '.join(list(map(str, sub_list)))
    print(test)