# 9. 자물쇠와 열쇠(풀이참조)

#배열(주소)를 인자값으로 넘기므로 리턴값 필요 없음
def check(arr, key, rotation, row, col):
  n=len(key)
  for i in range(n):
    for j in range(n): #회전 및 이동하며 열쇠와 자물쇠를 더함
      if rotation==0: 
        arr[row+i][col+j]+=key[i][j]  #회전x
      elif rotation==1:
        arr[row+i][col+j]+=key[n-1-j][i] # 90도 회전
      elif rotation==2:
        arr[row+i][col+j]+=key[n-1-i][n-1-j] # 180도 회전
      else:
        arr[row+i][col+j]+=key[j][n-1-i] #-90도 회전

def check2(arr, offset, n):
  for i in range(n):
          for j in range(n):
            if arr[offset+i][offset+j]!=1:
              return False
        
  return True
    

def solution(key, lock):
  offset=len(lock)-1 #(0,0)에서 떨어진 거리
  #열쇠를 돌려가며 나아가야할 범위
  for row in range(offset+len(lock)): 
    for col in range(offset+len(lock)):
      for rotation in range(4): #90도 씩 회전하며 돌아감
        arr=[[0]*58 for _ in range(58)] #자물쇠와 키의 크기가 최대 20까지 가능하므로 58x58배열 선언
        for i in range(len(lock)):
          for j in range(len(lock)):
            arr[offset+i][offset+j]=lock[i][j]
        check(arr,key,rotation,row,col)
        if check2(arr, offset, len(lock)):
          return True
        
  
  return False