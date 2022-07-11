#문자열 뒤집기

data= list(input())
convert_0=0 #0으로 뒤집는 횟수
convert_1=0 #1로 뒤집는 횟수
n=len(data)

for i in range(1, n):
    if(data[i]!=data[i-1]): #두번째 원소부터 시작, 전 원소와 달라지면
        if(data[i-1]=='0'): #조건에 따라 전원소의 값을 뒤집어줌
            convert_1+=1
        else:
            convert_0+=1

    # 전 원소에 대해서만 값을 뒤집어 주었기 때문에 마지막 영역도 조건에 따라
    # 값을 뒤집어줘야함
    if(data[n-1]=='0'):
        convert_1+=1

    else:
        convert_0+=1
#최소 값 구해야하므로 둘중 더 작은값을 뽑아주는 파이선 라이브러리
print(min(convert_0, convert_1))