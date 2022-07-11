#모험가 길드

n=int(input("입력해라"))

data=list(map(int, input().split()))

data.sort() #오름차순 정렬

i=0
count=0

while(n>0):

    if data[i]==1: #첫번째 값이 1이면 n에서 바로 빼기
        n=n-data[i]
        if n>0:
            count+=1
    #data[i+data[i]-1]는 현재 값과 같은 그룹으로 묶이는 마지막 값이다.
    if data[i]>1 and data[i]==data[i+data[i]-1]:
        n=n-data[i]
        if n>0:
            count+=1

    if data[i]>1 and data[i]<data[i+data[i]-1]:
        n=n-data[i+data[i]-1]
        if n>0:
            count+=1

    i+=1

print(count)