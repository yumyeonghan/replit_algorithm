#2. 미로 탈출

#2. 미로 탈출

from collections import deque

n, m= map(int, input().split())
data=[[0]*m for _ in range(n)]

for i in range(n):
  data[i]=list(map(int, input()))

#상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):

  count=1
  
    
  queue=deque()
  queue.append([x,y])
  
  while queue:
    x,y=queue.popleft()
    
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
  
      if nx>=0 and ny>=0 and nx<n and ny<m: 
        if data[nx][ny]==1:
          data[nx][ny]=data[x][y]+1
          print("nx= ", nx,"ny= ", ny, "값은= ",data[nx][ny])
          queue.append([nx,ny])
          
  
  return data[n-1][m-1]

print(bfs(0,0))
  
