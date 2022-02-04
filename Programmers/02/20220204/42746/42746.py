# 아이디어
#   - 배열안의 숫자를 문자형으로 바꾸어준다.(첫번째 문자의 크기에 따라 분류되기 때문)
#   - 문자열로 비교하기 때문에 비교할수 있는 최대값인 3자리 이상으로 비교하여 내림차순 정렬한다.
#   - 정렬된 배열을 join함수를 통해 하나의 문자열로 이어준다.
#   - (0으로만 이루어질 경우 0000은 0과 같은 의미이므로 다수의 0으로 이루어진 문자열은 0으로 바꾸어주어야한다.)
def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key = lambda x:x*3, reverse = True)
    answer = ''.join(numbers)
    answer = str(int(answer))
    return answer

numbers = [3, 30, 34, 5, 9]
answer = solution(numbers)
print(answer)

# <학습 포인트>
# 1. 배열안의 숫자를 변환하여 내림차순으로 정렬하는데까지는 성공했지만 다시 원래의 숫자로 바꾸는 방법에서 해맸다. 인터넷 포스팅을 보고서
#    배열안의 요소를 변환하지 않고 람다 함수를 통해 기준만 설정하여 정렬하는 방법을 알게 되었어다.