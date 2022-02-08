# 아이디어
#   - 동일한 중요도의 문서의 순서를 파악하기위해 priorities를 문자열로 바꿔준뒤 인덱스 번호를 붙여준다.
#   - max()를 통해 가장 현재 배열의 가장 중요한 중요도를 파악해준다.
#   - while문과 deque를 이용해 문자열 리스트를 하나씩 뺴어 중요도인 첫글자만 max()와 비교해준다.
#   - 중요도가 최댓값과 같은 경우 프린트한뒤(answer += 1) 프린트한 중요도는 remove해준다.
#   - 최대값과 다를 경우 다시 append해서 맨뒤로 보내준다.
#   - 만일 프린트한 인덱스 번호가 location과 같다면 break로 while문을 빠져나온뒤 프린트한 개수를 return해준다.

from collections import deque


def solution(priorities, location):
    answer = 0
    change = list(map(lambda x: str(x), priorities))
    for idx in range(len(change)):
        change[idx] = change[idx] + str(idx)

    deq = deque(change)

    while deq:
        cur = deq.popleft()
        if int(cur[0]) < max(priorities):
            deq.append(cur)
            continue
        if int(cur[0]) == max(priorities):
            if int(cur[1:]) == location:
                answer += 1
                break
            answer += 1
            priorities.remove(max(priorities))

    return answer

priorities, location = [1, 1, 9, 1, 1, 1] , 0
answer = solution(priorities,location)
print(answer)

# 제한 사항에 대기목록에는 1개이상 100개 이하의 문서이 있다고 하였다. 이러할 경우 내가 부여한 인덱스 번호가 두자리가 될 수 있다는 것을 고려하지 않았다.
# 그래서 프린트한 문서의 인덱스 번호를 구할 때, cur[-1]로 구했다. 내가 구하려는 인덱스번호가 아니라 인덱스 번호의 끝자리가 나와 인덱스 번호가 두자리로
# 넘어갈 경우 값을 찾지 못해 while문을 탈출하지 못하고 무한 루프를 돌게 되어 시간초과가 나왔다.
# 이를 해결하기 위해 첫번째 글자는 중요도 나머지는 인덱스 이므로 [1:]로 슬라이싱 하여 정확한 인덱스 값을 뽑고 시간초과 문제룰 해결하였다.