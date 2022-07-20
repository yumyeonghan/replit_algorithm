#9. 뱀

n=int(input())
maps=[[0]*n for _ in range(n)]

info_apple=int(input())
for _ in range(info_apple):
  low,col=map(int, input().split())
  #사과가 있으면 1
  maps[low-1][col-1]=1

nav={}

info_direct=int(input())
for _ in range(info_direct):
  l,c=map(str,input().split())
  nav[int(l)]=c

#동 남 서 북 
dy=[1,0,-1,0]
dx=[0,1,0,-1]

# 변경되는 방향
def change(direction,c):
  if c=="L":
    direction=(direction-1)%4 
  if c=="D":
    direction=(direction+1)%4

  return direction

def start():
  
  x,y=0,0
  
  #뱀이 걸친 장소는 2
  maps[x][y]=2
  direction=0
  time=0
  #뱀이 걸친 장소들 리스트
  q=[(x,y)]
  while True:
    nx=x+dx[direction]
    ny=y+dy[direction]

    #맵 범위안에 있고, 몸통에 부딪히지 않을때
    if 0<=nx and nx<n and 0<=ny and ny<n and maps[nx][ny]!=2:

      #사과가 있을때
      if maps[nx][ny]==1:
        maps[nx][ny]=2
        q.append((nx,ny))
      
      #사과가 없을때      
      if maps[nx][ny]==0:
        maps[nx][ny]=2
        q.append((nx,ny))
        px,py=q.pop(0) #꼬리 짜르기
        maps[px][py]=0

    #맵 또는 뱀 몸통에 부딪힐때
    else:
      time+=1
      break

    time+=1
  
    x=nx
    y=ny

    #현재 시간이 dictionary에 있다면 값을 보고 change함수 적용
    if time in nav:
      direction=change(direction, nav[time])
      
  return time

print(start())