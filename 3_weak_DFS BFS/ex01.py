#1. 음료수 얼려 먹기

n, m= map(int, input().split())
data=[[0]*m for _ in range(n)]
count=0

for i in range(n):
  data[i]=list(map(int, input()))

def dfs(x, y):
  if x<0 or y<0 or x>=n or y>=m:
    return False

  if data[x][y]==0:
    data[x][y]=1

    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    return True
  
  return False

for i in range(n):
  for j in range(m):
    if data[i][j]==0:
      if dfs(i,j)==True:
        count+=1

print(count)