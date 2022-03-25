'''
알파벳 대문자와 숫자(0-9)로만 구성된 문자열이 입력으로 주어집니다.
이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.
예를 들어 K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력합니다.
'''
#풀이1
list_data=input() #입력값 정렬할때 sorted()
list_real=[]
num=0
#A의 아스키 코드는 65부터 시작 즉,64보다 적게나오면 정수

#입력받은 문자열로부터 문자만 구해 리스트에 추가해주고 정렬
for list in list_data:
  if ord(list[0])>64:
    list_real.append(list[0])
  
list_real=sorted(list_real)

#숫자만 따로 뽑아 더해준뒤 리스트에 추가함 
for list in list_data:
  if ord(list[0])<65:
    num+=int(list[0])

list_real.append(str(num))
result=''.join(map(str,list_real))
print(result)

#풀이2

data=input()
result=[]
value=0

#문자를 하나씩 확인하며
for x in data:
  #알파벳인 경우 결과 리스트에 삽입
  if x.isalpha():
    result.append(x)
  #숫자는 따로 더하기
  else:
    value+=int(x)  

#알파벳 먼저 정렬하기
result=sorted(result)

#합한 숫자 리스트에 추가
result.append(str(value))

#리스트가 아닌 문자열로 출력
print(''.join(result))

  