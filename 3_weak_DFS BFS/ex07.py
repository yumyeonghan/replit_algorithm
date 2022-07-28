#7. 연산자 끼워 넣기

n=int(input())
a=list(map(int, input().split()))
연산=list(map(int, input().split()))

큰값=-100000000
작은값=100000000


def dfs(depth, answer, 더하기, 빼기, 곱하기, 나누기):
  
  global 큰값
  global 작은값

  
  if depth==n:   
      큰값=max(큰값, answer)
      작은값=min(작은값, answer)
      return

  if 더하기:
    dfs(depth+1, answer+a[depth],더하기-1,빼기,곱하기,나누기)
  if 빼기:
    dfs(depth+1, answer-a[depth],더하기,빼기-1,곱하기,나누기)
  if 곱하기:
    dfs(depth+1, answer*a[depth],더하기,빼기,곱하기-1,나누기)
  if 나누기:
    dfs(depth+1, int(answer/a[depth]),더하기,빼기,곱하기,나누기-1)

dfs(1 ,a[0],연산[0],연산[1],연산[2],연산[3])
print(큰값)
print(작은값)