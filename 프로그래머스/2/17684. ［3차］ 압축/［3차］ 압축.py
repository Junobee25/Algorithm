## 가장 긴 문자열 찾기
## 해당 문자열 제거
## 다음 글자 합친 후 단어 사전 등록


def solution(msg):
    alphabet = [chr(i).upper() for i in range(ord('a'), ord('z') + 1)] 
    alphabet_index = {}
    index = 27
    answer = []
    for i in range(len(alphabet)):
        alphabet_index[alphabet[i]] = i + 1
        
    flag = 0
    
    for i in range(len(msg)):
        tmp_list = []
        if (flag >= i and flag != 0):
            continue
        for j in range(i, len(msg)):
            if (msg[i : j + 1] in list(alphabet_index.keys())):
                tmp_list.append(msg[i : j + 1])
                flag = j
            else:
                alphabet_index[msg[i : j + 1]] = index
                index += 1
                break
                
        answer.append(alphabet_index[tmp_list[-1]])
                
            
    return answer
