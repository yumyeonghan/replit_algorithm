#6. 문자열 재정렬

list=list(input())
index=0
sum=0
list.sort() # 정렬하면 숫자 영어 순으로 정렬됨.

for i in range(len(list)):
      if list[i]=='1'or list[i]=='2' or list[i]=='3' or list[i]=='4' or list[i]=='5' or list[i]=='6' or list[i]=='7' or list[i]=='8' or               list[i]=='9':
        index+=1
        sum=sum+int(list[i])

del list[0:index] #del 함수를 이용해 숫자 제거
print(''.join(list)+str(sum)) #리스트를 문자열로 변환