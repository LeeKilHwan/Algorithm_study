# 아이디어
#   - deque를 이용하여 progresses와 speeds에서 요소 하나씩 꺼내 배포까지 걸리는 날짜를 계산한다.
#   - 구해진 배포까지의 날짜가 담긴 리스트를 반복문을 통해 앞의 과정이 완료되어 배포되면 배포되지 않은 과정까지의 과정을 countanswer리스트에 담아준뒤 반환해준다.

from collections import deque
def solution(progresses, speeds):
    answer = []
    work_day = []

    p_deq, s_deq = deque(progresses), deque(speeds)

    while p_deq:
        cur_work = p_deq.popleft()
        cur_speed = s_deq.popleft()
        for i in range(1, 101):
            cur_work += cur_speed
            if cur_work >= 100:
                work_day.append(i)
                break

    while work_day:
        remove_list = []
        a = work_day[0]
        cnt = 0
        for i in work_day:
            if i <= a:
                cnt += 1
                remove_list.append(i)
            else:
                break
        answer.append(cnt)
        for j in remove_list:
            work_day.remove(j)
    return answer

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
answer = solution(progresses,speeds)
print(answer)