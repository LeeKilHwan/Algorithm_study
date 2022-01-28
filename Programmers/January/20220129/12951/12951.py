def solution(s):
    answer = ''
    # 주어진 문자열 s를 split을 사용하여 공백을 쪼개준다.
    # (단 split()으로 할 경우 공백이 2개인경우를 하나로 인식하기때문에 split(' ')으로 해주어야 여러개의 공백을 각각 인식할 수 있다.)
    s = s.split(' ')

    # 공백을 기준으로 쪼갠 문자열을 capitalize를 통해 앞자리만 대문자 나머지는 소문자로 바꾸어준다.
    result_list = [word.capitalize() for word in s]

    # join을 통해 다시 쪼개주었던 공백을 기준으로 붙여 반환해준다.
    answer = " ".join(result_list)
    return answer

s = "3people unFollowed me"
answer = solution(s)
print(answer)