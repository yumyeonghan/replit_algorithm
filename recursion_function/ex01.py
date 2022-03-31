#재귀 함수, 마치 스택과 같은 원리로 동작한다.
#함수를 연속적으로 호출하면 컴퓨터 메모리 내부의 스택 프레임에 쌓인다.
#그래서 스택을 구현할 때 재귀함수를 이용하는 경우가 많다.
#for문과 재귀함수중 어느것이 적절한지 판단하고 이용하자 
def recursive_function(i):
  if i==100:
    return
  
  print(i,'번째 재귀함수에서', i+1, '번째 재귀함수를 호출합니다')

  recursive_function(i+1)

  print(i, '재귀함수를 종료합니다.')

recursive_function(1) 