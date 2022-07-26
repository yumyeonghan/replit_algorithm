# 3. 특정거리 도시 찾기

from collections import deque

n, m, k, x=map(int, input().split())
data=[[]*(n+1) for _ in range(n+1)]
for i in range(m):
  a,b=map(int, input().split())
  data[a].append(b)

print(data)

visited=[0]*(n+1)

queue=deque([x])

while queue:
    a=queue.popleft()
    
    for i in data[a]:
      if visited[i]==0:
        visited[i]=visited[a]+1
        queue.append(i)
        

for i in range(1, n+1):
  if visited[i]==k:
    print(i)

if k not in visited: 
  print(-1)


    