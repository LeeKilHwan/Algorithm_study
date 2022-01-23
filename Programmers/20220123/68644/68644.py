# 1.조합 라이브러리를 이용하여 주어진 배열에서 두개를 뽑을 수 있는 모든 경우의 수를 만들어준다.
# 2.뽑아준 두 수를 더한 값을 배열에 중복이 없이 담아주고 오름차순으로 정렬해준다.

from itertools import combinations


def solution(numbers):
    answer = []
    # 조합 라이브러리를 사용하여 리스트에서 중복없이 2개의 요소를 뽑는 모든 경우를 구해준다.
    cmb_list = list(combinations(numbers, 2))

    # 뽑아진 두수를 더한 값을 answer에 담아주고 중복된경우는 넘아가도록 해준다.
    for num in cmb_list:
        if sum(num) in answer:
            continue
        answer.append(sum(num))

    # 담아진 두수의 합의 경우의수를 오름차순으로 정렬해준다.
    answer.sort()
    return answer

numbers = [5,0,2,7]
answer = solution(numbers)
print(answer)
