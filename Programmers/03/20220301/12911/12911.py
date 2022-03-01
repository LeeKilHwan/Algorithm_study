# 아이디어
#   - 2진 변환하는 사용자 정의 함수를 만들어준다.
#   - 주어진 숫자 n을 이진수로 바꾼후 1의 개수를 센다
#   - n+1 부터 1000000까지 반복문을 돌면서 이진수로 변환했을때 1의 갯수가 n과 같은 수를 찾아 반환한다

def solution(n):
    answer = 0
    num = changed(n).count(1)
    cnt = 1

    for i in range(n + 1, 1000001):
        num2 = changed(i).count(1)
        if num == num2:
            answer = i
            break
    return answer


def changed(n):
    answer_list = []
    result = ""
    while n > 1:
        answer_list.append(n % 2)
        n = int(n / 2)
    answer_list.append(1)
    answer_list.reverse()
    return answer_list

n = 78
answer = solution(n)
print(answer)