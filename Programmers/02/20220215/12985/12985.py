# 아이디어
#    - n이 2의 몇승인지 구해준다. (이 토너먼트 경기는 2의 n승일 경우 n번만큼만 진행되기 때문)
#    - 경기 라운드 수인 n만큼 반복문을 돌려준다.
#    - 경기를 하게되는 번호는 2로 나누었을때 몫과 나머지가 같은 경우에만 경기를 하게된다.
#    - 또한 경기를 하게되면 새로운 번호를 달게 되는데 그 번호는 2로 나눈 몫과 나머지이다.
#    - 반복문을 통해 경기를 진행하다 A와B가 경기하게되는 라운드를 반환한다.

import math
def solution(n, a, b):
    answer = 0
    match_num = 0
    for i in range(1, 21):
        if math.pow(2, i) == n:
            match_num = i
            break

    for _ in range(match_num):
        answer += 1
        a = a % 2 + a // 2
        b = b % 2 + b // 2
        if a == b:
            break
    return answer

n, a, b = 8, 4, 7
answer = solution(n,a,b)
print(answer)