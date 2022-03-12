array=list(map(int, input().split()))
array.sort()

result=0 #그룹 수
count=0 #현재 그룹의 모함가 수

for i in array:
  count+=1
  if count>=i:
    result+=1
    count=0

print(result)