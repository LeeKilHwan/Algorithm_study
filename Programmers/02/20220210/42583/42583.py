# 아이디어
#   - 우선 다리의 길이만큼의 [0]의 개수로 이루어진 deque going_deq를 만들어준다.
#   - 대기 트럭에서 트럭 한대씩 다리위에 올라갈 수 있는지 무게를 판단해준다.
#   - 다리위로 올라갈 수 있는 경우에는 going_deq append해주고 popleft로 하나 뺴준다.
#   - 다리위로 올라갈 수 없는 경우에는 빈자리 0을 append해주고 popleft로 하나 뺴준다.
#   - 빼준 값이 0이 아닐 경우만 트럭이므로 0이 아닐 경우에만 finished_list에 append해준다.
#   - 주의사항 (최초의 다리의 무게를 변수로 정하고 트럭이 들어오고 나갈때 더하고 빼줘야 한다. )

from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0

    wait_deq = deque(truck_weights)
    going_deq = deque([0] * bridge_length)
    finished_list = []
    length = len(truck_weights)
    total = sum(going_deq)

    while True:
        if len(finished_list) == length:
            break

        if len(wait_deq) == 0:
            start = 0
        else:
            start = wait_deq[0]

        num2 = going_deq.popleft()
        if num2 > 0:
            finished_list.append(num2)
            total -= num2

        if total + start <= weight and start > 0:
            num1 = wait_deq.popleft()
            going_deq.append(num1)
            total += num1
        else:
            going_deq.append(0)
        answer += 1
    return answer

bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]
answer = solution(bridge_length,weight,truck_weights)
print(answer)



# 처음에는 다리위의 트럭의 무게를 sum()함수로 구하였다.
# sum()함수를 사용하면 while문을 돌때마다 sum()함수가 실행되고 다리의 길이가 길어지면 시간이 오래 걸리게 되어 시간초과로 몇몇 테스트 케이스를 통과하지 못하였다.
# 이러한 문제를 해결하기 위해 다리위의 무게를 변수로 설정하고 다리위에 트럭이 올라오면 트럭의 무게를 더해주고 트럭이 나가면 트럭의 무게를 빼주면 계산하는 회수가 줄어 시간을 단축 시킬수 있었다.