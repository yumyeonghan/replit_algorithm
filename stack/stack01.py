#스택 구현 예제
stack=[]
stack.append(1)
stack.append(5)
stack.append(2)
stack.append(6)
stack.append(8)
stack.append(4)
stack.pop()
print(stack[::-1])#처음부터 끝까지 -1칸(역순)간격으로 출력
print(stack)