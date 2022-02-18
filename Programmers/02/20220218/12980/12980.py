# 아이디어
#   - 주어진 수 n을 계속해서 2로 나누어준다.
#   - 2로 나누었을때 나머지가 존재하는 경우 -1해준다.
#   - -1을 해줄 경우 count해준다
#   - n이 0이 될때까지 반복한뒤 count한 수를 반환해준다.


def solution(n):
    answer = 0
    while n > 0:
        if n % 2 == 1:
            n = n - 1
            answer += 1

        else:
            n = n // 2
    return answer

n = 5000
answer = solution(n)
print(answer)