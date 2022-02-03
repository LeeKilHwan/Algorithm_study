def solution(n):
    answer = 0
    f_num = 0  # n보다 2작은수
    s_num = 1  # n보다 1작은수

    # 반복문을 통해서 숫자가 증가할 떄마다 2작은수와 1작은수의 값을 알맞게 바꾸면서 진행한다.
    for i in range(2, n + 1):
        answer = f_num + s_num
        f_num = s_num
        s_num = answer

    return answer % 1234567

n = 3
answer = solution(n)
print(answer)