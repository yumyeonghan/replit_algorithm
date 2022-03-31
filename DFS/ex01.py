'''
DFS는 깊이 우선 탐색으로 스택 혹은 재귀함수 를 이용한다.
1. 탐색 시작 노드를 스택에 삽입하고 방문처리 함
2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리함. 방문자히 않은 인접노드가 없으면 스택에서 최상단 노드를 꺼냄
3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복함.
'''
#DFS 메서드
def dfs(graph,v,visited):
  visited[v]=True
  print(v, end='')
  for i in graph[v]:
    if not visited[i]:
      dfs(graph,i,visited)

#각 노드가 연결된 정보 표현
graph=[[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

#각 노드가 방문 여부 표현
visited=[False]*9

#dfs 알고리즘 출력
dfs(graph,1,visited)