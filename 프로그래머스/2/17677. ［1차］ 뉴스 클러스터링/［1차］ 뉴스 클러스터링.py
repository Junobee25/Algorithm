import math
## 교집합
## 합집합

## 문자만 isalpha()
def solution(str1, str2):
    multiset1 = make_multiset(str1)
    print(multiset1)
    
    multiset2 = make_multiset(str2)
    return jacquard_similarity(multiset1, multiset2)



def make_multiset(arr):
    multiset = []
    
    for i in range(len(arr) - 1):
        if (arr[i:i+2].isalpha()):
            multiset.append(arr[i:i+2].upper())
                
    return multiset


def check_intersection(multiset1, multiset2):
    tmp = set()
    answer = 0
    for i in multiset1:
        if (i not in tmp and i in multiset2):
            answer += min(multiset1.count(i), multiset2.count(i))
        tmp.add(i)
    return answer
    
def check_union(multiset1, multiset2):
    
    return len(multiset1) + len(multiset2) - check_intersection(multiset1, multiset2)

    
def jacquard_similarity(multiset1, multiset2):
    if (check_union(multiset1, multiset2) == 0):
        return 65536
    else:
        answer = (check_intersection(multiset1, multiset2) / check_union(multiset1, multiset2)) * 65536
        return math.trunc(answer)
    
        