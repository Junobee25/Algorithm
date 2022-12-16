def solution(s):
    answer = []
    for i in range(len(s)):
        if s[i] in s[:i]:                    # i번째 요소가 i-1번째까지 요소들 중에 포함되어 있으면 실행
            while s[:i].count(s[i]) > 1:     # a[:i] 중에 a[i] 가 1개일 때 까지 반복
                s = s.replace(s[i],'0',1)    # a[i]를 '0'으로 1번만 바꿔서 초기화 하는 과정을 반복
            answer.append(i-s.index(s[i]))   # 갱신된 배열 a에서 i번째 요소와 처음 나오는 a[i]와 거리를 잰다 (중복되는 문자가 없기 때문에 최소 거리가 나옴)
        else:
            answer.append(-1)                # i번째 요소가 i-1번째까지 요소들 중에 포함되어 있지 않으면 -1 추가
    return answer