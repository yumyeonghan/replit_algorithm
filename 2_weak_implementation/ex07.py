#7. 문자열 압축

#아이디어 참고함

def solution(s):
    answer = len(s)
    #전체 길이의 절반으로 나눠질때 가장 크게 압축됨
    for step in range(1,len(s)//2+1):
        count=1
        fore=''
        pre=s[0:step]
        # 압축 크기별 묶어서 비교
        for i in range(step,len(s),step):
            if pre==s[i:i+step]:
                count+=1
            else: #이전 문자열과 비교해서 겹치면 count+1 함
                fore+=str(count)+pre if count>=2 else pre
                pre=s[i:i+step] #비교대상을 계속 초기화
                count=1
        #남은 문자 더해줌
        fore+=str(count)+pre if count>=2 else pre
        answer=min(answer,len(fore))
    return answer
  
s=input()
answer=solution(s)
print(answer)