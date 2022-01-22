# 1.문자열을 for문을 통해 자리마다 숫자일 경우, 문자일 경우를 판별하여 숫자는 빈 리스트에 담아주고,
#   문자는 문자에 맞는 연산작업을 진행해준다.
# 숫자일 경우 : 빈 리스트에 담아준다.
# 문자일 경우 : 문자가 의미하는 연산기호를 알맞게 빈 숫자를 담아준 리스트안에서 숫자를 연산해준다.
# (주의사항 : 숫자가 2자리일 경우의 예외 처리를 해주어야 한다.)

def solution(dartResult):
    answer = 0

    # 숫자가 10일 경우를 판독하기 위해 10을 문자 "A"로 치환해준다.
    dartResult = dartResult.replace("10", "A")

    # 숫자를 담을 빈 리스트 생성
    answer_list = []

    # 반복문을 통해 숫자와 문자를 구분해 알맞는 과정을 진행해준다.
    for i in dartResult:
        if i == "A":
            answer_list.append(10)
        elif i.isdecimal():
            answer_list.append(int(i))
        elif i == "D":
            answer_list[-1] = answer_list[-1] ** 2
        elif i == "T":
            answer_list[-1] = answer_list[-1] ** 3
        elif i == "#":
            answer_list[-1] = answer_list[-1] * (-1)
        elif i == "*":
            if len(answer_list) == 1:
                answer_list[0] = answer_list[0] * 2
            else:
                answer_list[-1] = answer_list[-1] * 2
                answer_list[-2] = answer_list[-2] * 2
    answer = sum(answer_list)
    return answer

dartResult = "1S2D*3T"
answer = solution(dartResult)
print(answer)