# 아이디어
#   - scoville을 heapq를 이용해 heap 자료구조로 바꾸어준다.
#   - 모든 음식을 스코빌 지수를 K이상으로 만들수 없는 경우는 1을 반환
#   - 나머지 경우는 heapq.heappop()을 통해 최소값을 꺼내 섞어준다
#   - (heap자료구조의 최소값이 K이하일경우 계속 반복)
#   - 스코빌 지수를 섞을 때마다 count 해준뒤 반환해준다.

import heapq

def solution(scoville, K):
    answer = 0
    li = []
    for value in scoville:
        heapq.heappush(li,value)
    while li[0] < K:
        if len(li) == 1 and li[0] < K:
            return -1
        heapq.heappush(li, heapq.heappop(li) + heapq.heappop(li) * 2)
        answer += 1
    return answer

scoville =  [1, 2, 3, 9, 10, 12]
K = 7
answer = solution(scoville, K)
print(answer)

# 처음에 효율성 측면에서 시간초과로 통과하지 못했다. 이유는 while min() < K 였다.
# min()은 전체중 최소값을 찾아야 하기 때문에 리스트 요소 전체룰 탐색하기 때문에 시간복잡도가 높아지게되었다.
# 결국 모든 스코빌 지수가 K 이상이면 되므로 li[0] < K 로 수정하여 시간초과문제를 해결하였다.