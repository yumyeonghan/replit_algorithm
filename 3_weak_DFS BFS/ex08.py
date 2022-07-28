#8. 감시 피하기

from itertools import combinations
n = int(input())
board= [] #전체 표
teachers = [] #선생님 위치
space = [] #빈공간

for i in range(n):
    board.append(list(map(str, input().split())))
    for j in range(n):
        if board[i][j]=="T":
            teachers.append([i,j])
        if board[i][j]=="X":
            space.append([i,j])

#선생 위치에서 4가지 방향으로 검사
def watch(x,y,directions):
    if directions==0: #왼쪽 검사
        while y>=0:
            if board[x][y]=="S":
                return True
            if board[x][y]=="O":
                return False
            y-=1
        
    if directions==1: #오른쪽 검사
        while y<n:
            if board[x][y]=="S":
                return True
            if board[x][y]=="O":
                return False
            y+=1
    
    if directions==2: #위쪽 검사    
        while x>=0:
            if board[x][y]=="S":
                return True
            if board[x][y]=="O":
                return False
            x-=1
    
    if directions==3: #왼쪽 검사    
        while x<n:
            if board[x][y]=="S":
                return True
            if board[x][y]=="O":
                return False
            x+=1

#학생이 걸리는지 검사
def check():
    for x, y in teachers:
        for i in range(4):
            if watch(x,y,i):
                return True
    return False

find=False
for data in combinations(space,3):
    for x,y in data:
        board[x][y]="O"
    if not check(): #학생이 감지되지 않았다면
        find=True
        break
    for x,y in data:
        board[x][y]="X"

if find:
    print("YES")
else:
    print("NO")