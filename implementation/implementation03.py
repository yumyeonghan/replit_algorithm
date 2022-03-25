'''
8 X 8 좌표 평면입니다. 나이트는 L자 형태로만 이동할 수 있으며 정원 밖으로는 나갈 수 없습니다.
나이트는 특정 위치에서 다음과 같은 2가지 경우로 이동할 수 있습니다.
1. 수평으로 두칸 이동한 뒤에 수직으로 한 칸 이동하기
2. 수직으로 두칸 이동한 뒤에 수평으로 한 칸 이동하기

이때 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성하세요 행 은 1부터 8로 표현하며, 열 은 a부터 h로 표현합니다.
a1에 있을 때 이동할 수 있는 경우의 수는 2가지 입니다.
c2에 있을 때 이동할 수 있는 경우의 수는 6가지 입니다.
'''

col,row=map(str,input())
row=int(row)

count_col=0
count_row=0

col_cmd=[1,-1] #오른쪽,왼쪽
row_cmd=[1,-1] #위,아래

if(col=='a'):
  col=1
if(col=='b'):
  col=2
if(col=='c'):
  col=3
if(col=='d'):
  col=4
if(col=='e'):
  col=5
if(col=='f'):
  col=6
if(col=='g'):
  col=7
if(col=='h'):
  col=8

#수평으로 2칸 먼저 갈때
for i in range(2):
 for j in range(2):
   nx=col+(col_cmd[i]*2)
   ny=row+row_cmd[j]
   if nx>0 and nx<9 and ny>0 and ny<9:
     count_col+=1

#수직으로 2칸 먼저 갈때
for i in range(2):
 for j in range(2):
   ny=row+(row_cmd[i]*2)
   nx=col+col_cmd[j]
   if nx>0 and nx<9 and ny>0 and ny<9:
     count_row+=1

count=count_col+count_row

print(count)