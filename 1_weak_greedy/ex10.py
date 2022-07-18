#무지의 먹방 라이브(풀이 참조한 것) 

import heapq

def solution(food_times, k):
    # answer를 못 구할 경우 -1 
    answer = -1
    # 힙 리스트
    hq = []
    # 힙리스트에 (섭취 시간, 순번)을 넣어준다.
    for i in range(len(food_times)):
        heapq.heappush(hq, (food_times[i], i+1))      
    length = len(hq)     # 음식 갯수 (한 사이클) 
    pre = 0  # 전 음식의 섭취 시간
    while hq:   # 리스트가 빌때까지
        # 가장 적은 섭취시간과 전 음식시간의 섭취시간을 빼주고, 음식 갯수를 곱해준다.
        diff = (hq[0][0] - pre) * length
        # 한사이클의 음식량을 빼줄 diff가 k보다 작거나 같으면 빼준다.
        if diff <= k:
            k -= diff
            # 한사이클을 돌렸기 때문에 해당 음식은 다먹었으니 제외 시킨다.
            length -= 1
            # 음식을 리스트에서 제외시키고, 해당 순서의 섭취시간을 변수에 업데이트 해준다.
            pre, _ = heapq.heappop(hq)
        # 한 사이클을 돌리지 못할때    
        else:
            # 한사이클을 돌리지 못하기 때문에 k와 남은 음식의 개수를 나눈 나머지가 해당 인덱스가 된다.
            idx = k % length
            # 현재 리스트가 섭취시간으로 정렬되어 있어서 두번째 값인 순번으로 정렬해준다.
            hq.sort(key = lambda x: x[1])
            # 답을 찾아주고 멈춰준다
            answer = hq[idx][1]
            break
    return answer