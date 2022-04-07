'''
N x M 크기의 직사각형 형태의 미로가 있다. 미로에는 여러 마리의 괴물이 있어 피해 탈출해야 한다.
현재 위치는 (1,1) 이며 미로의 출구는 (N,M)의 위치에 존재하며 한번에 한 칸씩 이동한다.
괴물이 있는 부분은0, 없는 부분은 1로 표시 되어 있고 이때 탈출하기 위해 움직여야 하는 최소 칸의 개수를
구하자. (칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.)
'''
from collections import deque

#BFS알고리즘
def bfs(x,y):
  queue=deque()
  queue.append((x,y))

  #큐가 빌 때까지
  while queue:
    x,y=queue.popleft()

    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]

      #좌표가 범위 밖일 경우 무시
      if  nx<0 or ny>=m or nx>=n or ny<0:
        continue

      #벽인 경우 무시
      if graph[nx][ny]==0:
        continue

      #해당 노드를 지나면 +1 해주고 기록
      if graph[nx][ny]==1:
        graph[nx][ny]=graph[x][y]+1
        queue.append((nx,ny))
  
  return graph[n-1][m-1]

n,m=map(int,input().split())

graph=[]

#2차원 배열 초기화
for i in range(n):
  graph.append(list(map(int,input())))

#이동 할 방향 상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

print(bfs(0,0))