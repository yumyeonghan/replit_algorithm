# 만들 수 없는 금액(풀이 참조 함)

n=int(input())

data= list(map(int, input().split()))

# 성취=목표-1
target=1

data.sort()

for i in data:
    # 데이터들의 값은 항상 타깃보다 작거나 같아야함
    # 그렇지 않으면 타깃이 성립하지 않음
    if target<i:
        break
    else:
        target+=i # 타깃+i 를 해주면 그 사이의 타깃들은 자연스레 성립 됨

print(target)
  