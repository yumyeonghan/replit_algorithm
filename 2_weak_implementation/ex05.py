#5. 럭키 스트레이트

number=input()

n=len(number)

sum_l=0
sum_r=0

for i in range(n//2):
  sum_l+=int(number[i])
  

for i in range(n//2,n):
  sum_r+=int(number[i])
  

if sum_l==sum_r:
  print("LUCKY")

else:
  print("READY")