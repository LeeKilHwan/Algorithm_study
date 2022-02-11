# 아이디어
#   - 문자열 number를 앞에서 부터 한자리씩 스택에 집어넣으면서 비교해준다.
#   - 우선 스택애 첫번째 자리 문자를 넣어준다.
#   - 두번째 자리 문자를 스택안의 문자와 비교해서 더 높은 숫자일 경우에 스택을 pop해주고 비교한 문자를 넣어준다.
#   - 비교한 문자가 작을경우 그대로 stack에 append해준다.
#   - 이 작업을 반복해서 문자열을 만들어주고 원래 문자열에서 k만큼 뺸 문자열을 반환해준다.


def solution(number, k):
    answer = ''
    stack = []
    for num in number:
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
        stack.append(num)
    stack = stack[:len(number) - k]
    answer = ''.join(stack)

    return answer
number = "4177252841"
k = 4
answer = solution(number,k)
print(answer)

# 처음 while문 없이 구현했었더니 한번 pop이 된 숫자는 더이상 연산이 이루어지지않아 몇몇 테스트 케이스에서 통화하지 못했다.
# 이러한 문제를 해결하기위해 while문을 사용해서 가장높은 숫자가 앞으로 올 수 있도록 하여 해결할 수 있었다.