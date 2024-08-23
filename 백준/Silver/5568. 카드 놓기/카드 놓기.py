from itertools import permutations

n = int(input())
k = int(input())
arr = [int(input()) for _ in range(n)]

test = set()

for s in permutations(arr, k):
    
    test.add(''.join(map(str, list(s))))
    
print(len(test))