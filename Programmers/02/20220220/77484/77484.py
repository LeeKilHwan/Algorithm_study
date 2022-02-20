# 아이디어
#    - 로또 번호가 맞아서 등수가 될수 있는 경우의 수로 배열 rank를 만들어준다.
#    - (맞춘 개수를 인덱스 번호하고 인덱스 번호의 등수로 배열을 만든다)
#    - 회손된 로또의 개수가 모두 맞을 경우 최대 등수가 되고 그렇지 않을 경우 최소등수가 된다.
#    - lottos에서 0의 개수를 세어서 lottos와 win_nums와 일치하는 값을 더하여 최대 등수를 만든다.
#    - lottos 에서 win_nums와 일치하는 값으로만 최소등수를 정한다
#    - 결과값을 반환해준다.


def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    cnt_0 = lottos.count(0)
    cnt = 0
    for i in range(6):
        if lottos[i] in win_nums:
            cnt += 1

    return [(rank[cnt_0 + cnt]), rank[cnt]]

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
answer = solution(lottos, win_nums)
print(answer)