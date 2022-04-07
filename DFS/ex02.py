'''
N(가로) x M(세로) 크기의 얼음 틀이 있습니다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하세요.
'''

#DFS 로직 설정
def dfs(x,y):
  if x<=-1 or x>=row or y<=-1 or y>=col:
    return False  
  #현재 노드가 0으로 방문하지 않았으면 1로 바꾸고 실행
  if graph[x][y]==0:
    graph[x][y]=1
    graph[x][y]=1
    #상하좌우로 돌아다니면서 BFS탐색
    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    return True
  return False

graph=[]
result=0
row,col=map(int,input().split())
for _ in range(row):
  graph.append(list(map(int,input())))

for i in range(row):
  for j in range(col):
    a=dfs(i,j)
    #DFS탐색시 첫 true값 리턴한 함수만 1씩 카운팅함
    if a==True:
      result+=1
print(result)