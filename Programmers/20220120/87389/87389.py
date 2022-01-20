# n보다 작은수로 나누었을때 나머지가 0이 되는 수들을 빈 리스트에 담아준다.
# 리스트에서 최소값을 반환해준다.

def solution(n):
    answer = 0
    for i in range(1, n):
        if n % i == 1:
            answer = i
            break
    return answer

a = solution(10)
print(a)