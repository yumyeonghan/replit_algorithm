#5. 경쟁적 전염

from collections import deque

n,k=map(int, input().split())
graph=[]
for _ in range(n):
  graph.append(list(map(int, input().split())))

s, x, y=map(int,input().split())

#상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def solution(s,a,b,k):
  time=1
  count=0
  queue=deque()
  
   #k 가 1일때부터 k일때 까지 값을 찾고 차례대로 큐에 넣어준다.
  #k 는 1부터 큐에 들어가기떄문에 항상 작은게 먼저 확장됨
  # k=3이라 가정하면 1->2->3 순으로 확장됨
  for k in range(1,k+1):
    for i in range(n):
      for j in range(n):
        if graph[i][j]==k:
          queue.append([i,j])
      
  print(queue)        

  #bfs 사용
  while queue:
    x,y=queue.popleft()
    # 현재 그래프에 0의 개수가 몇갠지 파악
    for i in range(n):
      for j in range(n):
        if graph[i][j]==0:
          count+=1
    #상하좌우로 움직임
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if count>=k: # 0의 개수가 k개 미만이면 실행x(바이러스가 동시에 움직이기 떄문)
        # 
        if nx>=0 and nx<n and ny>=0 and ny<n:
          if graph[nx][ny]==0: #작은 바이러스가 먼저 들어오면 큰 바이러스는 들어오지못함
            graph[nx][ny]=graph[x][y]  
            queue.append([nx,ny])
    count=0
          
  print(graph)
  return graph[a][b]
    
  
  
    

print(solution(s,x-1,y-1,k))


