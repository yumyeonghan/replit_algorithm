#6. 괄호변환

def divide(p):
    count_l=0
    count_r=0
    for i in range(len(p)):
        if p[i]=="(":
            count_l+=1
        else:
            count_r+=1
        if count_l==count_r:
            return p[:i+1], p[i+1:]
        

def check(p):
    stack=[]
    for i in range(len(p)):
        if p[i]=="(":
            stack.append(p[i])
        else:
            if not stack:
                return False
            stack.pop()
    return True
    

def solution(p):
    answer=""
    #1 빈 문자열 반환
    if p=="":
        return ""
    
    #2 u,v로 분리, return 값으로 2개를 넘겨주면 됨
    u,v=divide(p)
    
    #3 u가 올바른 문자라면
    #3-1 u에 이어 붙여 반환(v에대해 1단계부터 재귀함수 호출) 
    if check(u):
        return u+solution(v)
    
    
    
    else:#4 u가 올바른 문자가 아니라면
        answer+="("#4-1 빈 문자열에 첫번째 문자로 "(" 붙임
        answer+=solution(v) #4-2
        answer+=")"#4-3
        
        #4-4
        for i in u[1:-1]:
            if i=="(":
                answer+=")"
            else:
                answer+="("
        
        return answer
            
        
        
    
        
    
    
    return answer