# 1. 배열을 정렬해준다.
# 2. 정렬된 배열에서 예산을 초과하는 금액을 요청한 부서는 제거해준다.
# 3. 반복무을 통해 작은 리스트요소를 예산에서부터 빼준뒤 뺸 숫자를 반환해준다.
# 4. 예산이 -가 된다면 그 직전까지의 뺀 수자를 반환해준다.

from itertools import combinations


def solution(d, budget):
    answer = 0

    d.sort()
    for bg in d:
        budget = budget - int(bg)

        if budget < 0:
            budget = budget + bg
            break

        answer += 1
    return answer

d = [1,3,2,5,4]
budget = 9
answer = solution(d,budget)
print(answer)