#숫자 카드 게임

row, col=map(int,input("2개 입력해라").split()) # 행 열 입력
result=[[0]*row for _ in range(col)] # 2차원 배열 초기화
max=0

for i in range(row):
    data=list(map(int, input("3개 입력해라").split())) 
    result[i]=data # 입력한 데이터 값을 각 행에다 넣어줌.
    result[i].sort() # 오름차순 정렬 
    
    if(max<result[i][0]):  
        max=result[i][0] #가장 작은 값 중에 큰 값 선택

print(max)
