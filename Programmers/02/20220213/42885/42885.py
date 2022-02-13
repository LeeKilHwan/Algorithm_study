# 아이디어
#   - 배열을 내림차순 정렬한다.
#   - 배열을 deque안에 담아준다.
#   - deque안의 가장 큰수와 가장 작은수를 더해 제한무게를 초과하지 않는 경우 둘다 pop해준다 (pop할 경우 answer에 1을 더해준다.)
#   - 제한 무게를 초과한 경우 큰수만 pop해준다.(pop할 경우 answer에 1을 더해준다.)
#   - deque안의 모든 수가 사라질때 까지 반복해준뒤 answer을 반환해준다.

from collections import deque

def solution(people, limit):
    answer = 0
    people = deque(sorted(people, reverse=True))
    weight = 0
    while people:
        weight = people[0]
        if weight + people[-1] <= limit:
            people.pop()
            people.popleft()
            answer += 1

        else:
            people.popleft()
            answer += 1

        if people and people[0] <= (limit // 2):
            answer += (len(people) // 2 + len(people) % 2)
            break
    return answer

people = [70, 50, 80, 50]
limit = 100
answer = solution(people, limit)
print(answer)


# 처음에 deque를 이용하지 않고 stack으로 popleft()를 pop(0)으로 사용하여 문제를 풀었다.
# 아무리 코드를 고쳐도 효율성 테스트에서 시간초과를 해결할 수 없었다.
# 안됬던 이유 : list에서 pop()은 O(1)의 시간복잡도를 가지고 있고 pop(0)은 O(N)의 시간복잡도를 가지고 있기 때문에 계속 효율성 테스트에서 시간초과가 나왔다.
# 이를 해결하기 위해 deque라이브러리를 가져와 popleft()를 사용하여 시간초과를 해결할 수 있었다.

# <더 나은 풀이>
# def solution(people, limit) :
#     answer = 0
#     people.sort()
#
#     a = 0
#     b = len(people) - 1
#     while a < b :
#         if people[b] + people[a] <= limit :
#             a += 1
#             answer += 1
#         b -= 1
#     return len(people) - answer
#
# deque를 사용하지않고 두개의 포인터를 가장 작은수와 마지막 수의 인덱스 번호로 하나씩 증가, 감소를 통해 비교하는 방법을 사용하였다.
# 이 경우 간단한 연산 작업만 일어나게 되므로 효율성 측면에서 훨씬 나은 방법이라 생각된다.