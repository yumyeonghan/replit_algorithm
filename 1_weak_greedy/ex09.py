# 볼링공 고르기

n, m= map(int, input("입력").split())

data=list(map(int, input().split()))

count=0

for i in range(len(data)):
    for j in range(i+1, len(data)):
        if(data[i]!=data[j]):
            count+=1

print(count)