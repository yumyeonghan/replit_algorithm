# 당장 좋은 것만 선택하는 그리디
# 잔돈을 동전값이 큰것부터 우선으로 나눠주면서 동전 갯수 카운팅 해주고
# 잔돈은 계속 최신화 해줌으로서 500원 부터 10원까지 작업 해줌

change=1230 #거슬러줘야 할 돈
count=0     #동전의 총 개수

if(change//500>0): 
  count+=change//500
  change=change%500

if(change//100>0):
  count+=change//100
  change=change%100

if(change//50>0):
  count+=change//50
  change%=50

if(change//10>0):
  count+=change//10
  change%=10

print("거슬러줘야 할 동전의 최소 개수는", count)