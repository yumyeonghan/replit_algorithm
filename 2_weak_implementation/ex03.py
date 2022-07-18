#3. 왕실의 나이트

x,y=input()
y=int(y)
list=['a','b','c','d','e','f','g','h']

vector_x=[-1,1] #왼쪽 오른쪽
vector_y=[-1,1] #위쪽 아래쪽

count=0

# a~h 를 1~8 로 바꿈
for i in range(len(list)):
  if list[i]==x:
    x=i+1


# 오오위 오오아 왼왼위 왼왼아
for i in range(len(vector_x)):
  for j in range(len(vector_y)):
    if (1<=x+vector_x[i]+vector_x[i]<=8 and 1<=y+vector_y[j]<=8):
      count+=1
     
      
#위위왼 위위오 아아왼 아아오
for i in range(len(vector_y)):
  for j in range(len(vector_x)):
    if (1<=y+vector_y[i]+vector_y[i]<=8 and 1<=x+vector_x[j]<=8):
      count+=1
      
print(count)

    
    
