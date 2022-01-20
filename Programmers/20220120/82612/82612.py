# <풀이 방법>
#   1. 놀이기구를 현재 가지고 있는 돈에서 이용한 회차에 따른 금액을 반복해서 빼준다 (반복문 사용))
#   2. 남아있는 돈이 양수이면 0을 반환해주고, 움수일 경우에는 절대값을 반환해준다.

def solution(price, money, count):
    answer = -1
    for cnt in range(1, count + 1):
        money = money - (price * cnt)
    if money >=0 :
        answer = 0
    else:
        answer = abs(money)
    return answer

answer = solution(3,20,4)
print(answer)