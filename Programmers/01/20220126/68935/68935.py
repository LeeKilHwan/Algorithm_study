# 1. 주어진 수를 3진법으로 바꾸어 준다.
# 2. 3진법으로 바꾼 숫자를 뒤집어준다.
# 3. 뒤집힌 3진법을 다시 10진법으로 바꾸어 준다

def solution(n):
    answer = 0
    answer_list = []
    cnt = 0
    # 3진법으로 바꾸었을 때 자리수를 계산해준다.
    while n >= (3 ** cnt):
        cnt += 1

    # 3진법으로 바꾸어 각 자리수를 answer_list에 담아준다.
    for i in range(cnt - 1, -1, -1):
        answer_list.append(int(n // (3 ** i)))
        n = n % (3 ** i)
    # 담아진 요소를 거꾸로 반환하여 answer에 더해준다.
    for j in range(len(answer_list)):
        answer += answer_list[j] * (3 ** j)

    return answer

n = 45
answer = solution(n)
print(answer)