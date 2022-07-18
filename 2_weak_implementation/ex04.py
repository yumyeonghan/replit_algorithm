#4. 게임 개발
move_x1=True
move_x2=True
move_y1=True
move_y2=True

count=1 #방문한 칸

n,m=map(int, input().split())

x,y,v=map(int, input().split())

data=[[0]*n for _ in range(m)]

for i in range(m):
  data[i]=list(map(int, input().split()))

vector=[-1, 1, 1, -1] #북 동 남 서

while data[x][y]!=1: #뒤로 갔을때 바다면 종료
  for i in range(len(vector)): #북 동 남 서 순으로 한칸 이동시 바다가 아닐경우 움직임(움직일 경우 방문 횟수+1) 
    if i==0 or i%2==0 :
      if data[x+vector[i]][y]!=1:
        data[x][y]=1 # 머물렀던 장소는 1로 바꿔준다.
        x=x+vector[i]
        count+=1
      #바다라 움직일수 없을경우 false로 바꿔줌
      else:
        move_x1=False
        move_x2=False
     
    else:
      if data[x][y+vector[i]]!=1:
        data[x][y]=1
        y=y+vector[i]
        count+=1

      else:
        move_y1=False
        move_y2=False

    if move_x1==False and move_y1==False and move_x2==0 and move_y2==0: #상하좌우 전부 갈수 없을때
      # 바라보는 방향의 반대(뒤칸)으로 움직임
      if i==0:
        x=x+1
      elif i==1:
        y=y-1
      elif i==2:
        x=x-1
      else:
        y=y+1
  
  #탐색이 한번 끝나면 복구
  move_x1=True
  move_x2=True
  move_y1=True
  move_y2=True

  print("test")
  
print(count)