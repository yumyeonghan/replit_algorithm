#10. 기둥과 보 설치

pillar = [[]]
bar = [[]]

def check_pillar(x,y):
    if y==0 or pillar[x][y-1]:
        return True
    if (x>0 and bar[x-1][y]) or bar[x][y]:
        return True
    return False

def check_bar(x,y):
    if (y>0 and pillar[x][y- 1]) or pillar[x+1][y-1]:
        return True
    if x>0 and bar[x-1][y] and bar[x+1][y]:
        return True
    return False

def delete(x,y):
    
    for i in range(x-1, x+2):
        for j in range(y, y+2):
            if pillar[i][j] and check_pillar(i, j)==False:
                return False
            if bar[i][j] and check_bar(i,j)==False:
                return False
    return True

        
        

def solution(n, build_frame):
    global pillar, bar
    pillar= [[0]*(n+2) for _ in range(n+2)]
    bar = [[0]*(n+2) for _ in range(n+2)]
    answer=[]
    
    for x, y, a, b in build_frame:
        if a==0:
            if b==1:
                if check_pillar(x, y):
                    pillar[x][y]=1
            else:
                pillar[x][y]=0
                if not delete(x, y):
                    pillar[x][y]=1
        else:
            if b==1:
                if check_bar(x, y):
                    bar[x][y]=1
            else:
                bar[x][y]=0
                if not delete(x, y):
                    bar[x][y]=1
    
    for x in range(n+1):
        for y in range(n+1):
            if pillar[x][y]==1:
                answer.append([x,y,0])

            if bar[x][y]==1:
                answer.append([x, y, 1])

    return answer


 