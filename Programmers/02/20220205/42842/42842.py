# 아이디어
#   - brown과 yellow를 더해서 전체 카펫의 넓이를 구해준다.
#   - for문을 통해 가로를 확한다. numd으로 나눠지면 num 가로, h는 세로
#   - (num-2)(h-2)가 yellow이면 [num, h]를 반환한다.

from itertools import combinations

def solution(brown, yellow):
    answer = []
    total = brown + yellow

    for num in range(total, 2, -1):
        if total % num == 0:
            x = total // num
            if (num - 2) * (x - 2) == yellow:
                answer = [num, x]
                break

    return answer

brown, yellow = 24, 24
answer = solution(brown, yellow)
print(answer)


# <처음 풀었던 풀이>

# from itertools import combinations
#
# def solution(brown, yellow):
#     answer = []
#     total = brown + yellow
#     answer_list = []
#
#     for i in range(1, total + 1):
#         if total % i == 0:
#             answer_list.append(i)
#     answer_list.reverse()
#
#     if len(answer_list) % 2 == 0:
#         cmb = list(combinations(answer_list,2))
#         cmb = list(filter(lambda x:x[0]*x[1] == total,cmb))
#         cmb = list(filter(lambda x:(x[0]-2) * (x[1] -2) == yellow,cmb))
#         for i in cmb:
#             answer = list(i)
#     else:
#         answer = [answer_list[1]] * 2