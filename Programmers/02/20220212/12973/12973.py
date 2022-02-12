# 아이디어
#   - 주어진 문자열을 앞에서부터 하나씩 꺼내서 stack에 담아준다.
#   - stack에 담긴 문자와 문자열에서 꺼낸 문자를 비교하여 같을경우 pop()
#   - stack에 담긴 문자와 문자열에서 꺼낸 문자를 비교하여 다를경우 append해준다.
#   - 모든 문자를 비교한후 stack에 값이 들어있다면 0 값이 없다면 1을 반환해준다.


def solution(s):
    answer = -1
    stack = []

    for word in s:
        if len(stack) == 0:
            stack.append(word)
        else:
            if stack[-1] == word:
                stack.pop()
            else:
                stack.append(word)
    if stack:
        answer = 0
    else:
        answer = 1
    return answer

s = "baabaa"
answer = solution(s)
print(answer)


# 처음 문제를 풀었을때 주어진 문자열을 stack에 담아 하나씩 꺼내어 while문으로 비교를 진해하였다.
# 이 경우 시간초과 문제로 효율성 테스트를 통과하지 못했다. 이를 해겨하기위해 주어진 문자열을 stack으로 만들지 않고 for문을 통해 문자하나하나
#바로 비교할 수 있도록 하여 시간초과를 해결하고 효율성 테스트에서도 통과할 수 잇었다.