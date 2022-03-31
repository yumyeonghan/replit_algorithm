#큐 구현
from collections import deque #큐를 구현하기 위해 deque 라이브러리 사용

queue=deque()
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
queue.popleft() #제일 먼저 들어온 것 부터 pop 시킴, 1 제외
queue.popleft() #제일 늦게 들어온 것 부터 pop 시킴, 2 제외
print(queue)
queue.reverse() #거꾸로 출력
print(queue)

