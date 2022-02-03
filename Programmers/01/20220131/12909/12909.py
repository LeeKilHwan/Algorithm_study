def solution(s):
    answer = True
    temp = 0  # 괄호의 짝이 맞추어 졌는지에 대한 여부를 담아준다.(0일때 짝이 맞춰졌다는 뜻이다.)

    # ')'일 경우 -1을 , '('일 경우 +1을 temp에 담아준다.
    for i in s:
        if i == ")":
            temp -= 1
        else:
            temp += 1
        if temp < 0:
            return False
    # temp 가 0보다 클 경우 '('가 더 많다는 뜻이므로 짝이 맞지 않는다.
    if temp > 0:
        return False
    return True

s = "(()("
answer = solution(s)
print(answer)