# 배열안의 가장 큰수를 기준으로 설정한다
# 기준이 되는 수를 배열안의 모든 원소를 나누어준다.
# 모두 나누어 떨어지지 않을 경우 기준이 되는 수를 기준값만큼 증가시켜 다시 진행한다.
# 모두 나누어 떨어지게되면 최소 공배수가 되므로 현재 숫자를 반환해준다.

def solution(arr):
    answer = 0
    # 배열안의 가장 큰 수를 기준값으로 설정해준다.
    max_num = max(arr)
    temp = max_num

    # 최댓값을 배열안의 원소로 나누어준다. 모두 나누어 떨어지지 않을 경우 최대값만큼씩 계속 더해서 진행해준다.
    while True:
        cnt = 0
        for num in arr:
            if temp % num == 0:
                cnt += 1
        if cnt == len(arr):
            break

        temp += max_num
    answer = temp
    return answer

arr = [2, 6, 8, 14]
answer = solution(arr)
print(answer)
