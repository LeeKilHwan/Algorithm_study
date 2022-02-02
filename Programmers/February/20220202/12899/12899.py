# 주어진 숫자를 3진법으로 바꾸어준다.
# 3진법으로 바꾸어진 수에서 0을 4로 바꾸어준다.
# 0을 4로 바꾸게 될경우 바로 앞 숫자를 4일경우 -2 나머지 경우 -1로 바꾸어준다.
# 최종으로 바뀌어진 숫자에서 맨 앞자리가 0일 경우 0을 제거해준뒤 반환해준다.

def solution(n):
    # 구현해둔 메소드를 이용하여 주어진 수를 3진법으로 변환된 베열 형태로 반환
    answer = change(n)

    # 반복문을 통해 0을 4로 바꾸어주고 바로 직전의 숫자를 변환해준다.
    while 0 in answer:
        for i in range(len(answer)):
            if answer[i] == 0:
                answer[i] = 4
                if answer[i - 1] == 4:
                    answer[i - 1] = answer[i - 1] - 2
                else:
                    answer[i - 1] = answer[i - 1] - 1
        if answer[0] == 0:
            answer.remove(0)

    # 더했을때 1,2,4로 표현될 수 있도록 리스트 안의 정수 요소를 문자형으로 바꾸어준다.
    answer = list(map(lambda x: str(x), answer))

    # 모든 과정을 통해 변환된 최종 리스트를 반환해준다.
    result = ''
    for word in answer:
        result += word
    return result


# 주어진 숫자를 3진법으로 바꾸는 상용자 정의 함수 구현.
def change(n):
    changed_list = []
    while True:
        if n < 3:
            changed_list.append(n % 3)
            break
        if int(n / 3) == 1:
            changed_list.append(n % 3)
            changed_list.append(1)
            break
        changed_list.append(n % 3)
        n = int(n / 3)
    changed_list.reverse()

    return changed_list

n = 17
answer = solution(n)
print(answer)