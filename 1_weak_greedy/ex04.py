#1이 될때까지

n,k=map(int, input("입력하시오.").split())
count=0
while n!=1: 
    if n%k==0:
        n=n//k
        count+=1
    else:
        n=n-1
        count+=1

print(count)