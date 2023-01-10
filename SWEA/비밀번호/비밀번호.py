for i in range(10):
    cnt = 0  # 인덱스 조절
    N,password = input().split()
    pw = list(map(str,password))
    while pw:
        cnt += 1
        if cnt >= len(pw):  # 조건에따라 비밀번호화 시킨 배열의 길이보다 인덱스가 커져버리면 break
            break
        if pw[cnt] != pw[cnt-1]:  # 앞칸 요소와 다르면 pass
            pass
        else:   # 앞칸요소와 똑같으면
            cnt-=2  # 인덱스를 땡겨주고
            pw.pop(cnt+2)  # 해당요소와 앞칸 요소를 삭제시켜 나감
            pw.pop(cnt+1)
        
    print('#'+str(i+1)+' '+''.join(pw))  # 리스트를 문자열로 출력
