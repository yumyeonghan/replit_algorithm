#곱하기 혹은 더하기

n=list(input())
result=0


for i in n:

  # 문자로 받은 리스트를 정수로 변환해줌.
  i=int(i)
  
  #만약 값이 0이거나 1이면 이 값을 더해줌.
  #지금까지 나온 결과가 0이면 다음 값과 더해준다. 
  if i==0 or i==1 or result==0 or result==1:
    result+=i
    print(result)

  else:
    result*=i

print(result)