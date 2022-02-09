#  아이디어
#   - deque를 이용하여 맨 처음의 숫자를 현재 주가로 설정
#   - 반복문을 통해 prices를 돌면서 현재 주가에서 떨어지지 않을 경우에만 +1해준다.
#   - count한 숫자를 answer 리스트에 append해준다.

from collections import deque


def solution(prices):
    answer = []
    deq = deque()
    for i in prices:
        deq.append(i)
    while deq:
        cur_num = deq.popleft()
        cnt_num = 0
        for cnt in deq:
            cnt_num += 1
            if cur_num > cnt:
                break
        answer.append(cnt_num)

    return answer

prices = [1, 2, 3, 2, 3]
answer = solution(prices)
print(answer)