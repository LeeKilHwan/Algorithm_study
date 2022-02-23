# 아이디어
#   - 모든 0을 제거해준뒤 제거한 0을 count해준다
#   - 이진 변환활때마다 count 해준다.
#   - 이전 변화된 개수와 제거된 0의 숫자를 반환해준다.

def solution(s):
    answer = []
    cnt_0 = 0
    cnt_round = 0
    while s != "1":
        cnt_0 += s.count("0")
        s = s.replace("0",'')
        s = change(len(s))
        cnt_round += 1
    answer = [cnt_round, cnt_0]
    return answer

# 이진수로 변환해주는 사용자 함수 정의
def change(num):
    result = 0
    result_list = []
    while num > 1:
        result_list.append(str(num % 2))
        num = num // 2
    result_list.append(str(1))
    result_list.reverse()
    result = ''.join(result_list)
    return result

s = "110010101001"
answer = solution(s)
print(answer)

# 파이썬의 내장함수로 이진수를 반환해주는 함수 bin을 이용하면 훨씬 간결하게 문제를 해결할 수 있었다.

# def solution(s):
#     answer = []
#     cnt_0 = 0
#     cnt_round = 0
#     while s != "1":
#         cnt_0 += s.count("0")
#         s = s.replace("0",'')
#         s = bin(len(s))[2:]
#         cnt_round += 1
#     answer = [cnt_round, cnt_0]
#     return answer
