from itertools import permutations

def solution(user_id, banned_id):
    user_permutation = list(permutations(user_id, len(banned_id)))
    ban_list = []
    
    for users in user_permutation:
        if not check_id(users, banned_id):
            continue
        
        users = set(users)
        if users not in ban_list:
            ban_list.append(users)
    return len(ban_list)

def check_id(users, banned_id):
    for i in range(len(users)):
        if (len(users[i]) != len(banned_id[i])):
            return False
        
        for j in range(len(users[i])):
            if (banned_id[i][j] == '*'):
                continue
            if (users[i][j] != banned_id[i][j]):
                return False
    return True
            