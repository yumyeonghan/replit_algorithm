# 입력값
# 배열의 크기 n
# 숫자 더하는 횟수 m
# 특정 인덱스 값의 중복 더하기 제한 횟수 k 
# N 개의 자연수

n, m, k=map(int,input("입력해라").split())
data= list(map(int, input().split()))
result=0
data.sort(reverse=True)
print(data)

while m!=0:
    for i in range(k):
        result+=data[0]
        m-=1
        if(m==0):
            break

    result+=data[1]
    m-=1

print(result)
