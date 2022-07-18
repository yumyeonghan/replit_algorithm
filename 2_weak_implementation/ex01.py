#1. 상하좌우

number=int(input("숫자를 입력하세요"))
list=list(map(str,input().split()))
x=1
y=1

for i in range(len(list)):
    if(list[i]=="L"):
        if(y-1>=1):
            y-=1
    if(list[i]=="R"):
        if(y+1<=number):
            y+=1
    if(list[i]=="U"):
        if(x-1>=1):
            x-=1
    if(list[i]=="D"):
        if(x+1<=number):
            x+=1

print(x,y)
        
