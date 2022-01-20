import math

def solution(n):
    answer = 0
    # 에라토스테네스의 체 알고리즘 활요하여 풀어야한다
    result_list = []

    #
    answer_list = [0] * (n + 1)

    for i in range(2, int(math.sqrt(n)) + 1):

        if answer_list[i] == 0:
            cnt = 2
            while i * cnt <= n:
                answer_list[i * cnt] = 1
                cnt += 1

    print(answer_list)
    for num in range(2, len(answer_list)):
        if answer_list[num] == 0:
            result_list.append(answer_list[num])
    answer = len(result_list)

    return answer