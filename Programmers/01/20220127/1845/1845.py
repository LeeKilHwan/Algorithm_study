def solution(nums):
    answer = 0
    answer_list = []  # 선택한 포켓몬을 담아줄 리스트

    # 이미 담은 포켓몬이 있을 경우에는 continue로 배재해준다.

    # 데려갈 수 있는 포켓몬 종류의 최대값은 데려갈 수 만큼의 포켓몬이므로 배열안에 데려갈 수 있는 포켓몬
    # 이 모두 차게될 경우 배열을 끝내고 배열안의 포켓몬 종류를 반환해준다.
    for select in nums:
        if select in answer_list:
            continue
        answer_list.append(select)
        if len(answer_list) == (len(nums) / 2):
            break
    answer = len(answer_list)
    return answer

nums = [3,1,2,3]
answer = solution(nums)
print(answer)