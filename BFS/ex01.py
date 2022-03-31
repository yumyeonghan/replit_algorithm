'''
BFS는 너비 우선 탐색 이며 큐 자료구조를 이용한다.
1. 탐색 시작 노드를 큐에 삽입하고 방문 처리함.
2. 큐에서 노드를 꺼낸 뒤 해동 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리함.
3. 2번 과정을 수행할 수 없을 때까지 반복함.
BFS는 가까운 것 부터 탐색을 함->각 간선의 비용이 같다면 최단 거리 문제를
해결하기 위한 목적으로 사용될 수 있다.
'''
#BFS 메서드 정의
from collections import deque
def bfs(graph,start,visited):
  #큐 구현 위해 데큐 라이브러리 사용
  queue=deque()
  #현재 노드 방문 처리
  queue.append(start)
  visited[start]=True
  #큐가 빌 때까지 반복
  while queue:
    v=queue.popleft()
    print(v,end="")
    #아직 방문하지 않은 인접한 원소들 큐에 삽입
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i]=True
        

#각 노드가 연결된 정보 표현
graph=[[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

#각 노드가 방문 여부 표현
visited=[False]*9

#bfs 알고리즘 출력
bfs(graph,1,visited)