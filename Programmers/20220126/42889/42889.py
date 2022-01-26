def solution(N, stages):
    answer = []
    dic = {}
    allPlayers = len(stages)
    # 각 단계별 실패율을 dictionary형으로 담아준다.
    for i in range(1, N + 1):
        # 스테이지에 도달한 유저가 없는 경우 0으로 처리해주어야 한다.
        if allPlayers == 0:
            rate = 0
        else:
            rate = stages.count(i) / allPlayers
        dic[i] = rate
        allPlayers -= stages.count(i)

    # 실패율인 dictionary의 value값으로 sorted와 lambda를 사용하여 내림차순으로 정렬해준다.
    sort_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)


    # 순서에 맞게 정렬된 dictionary의 키값을 리스트에 담아 반환해준다.
    answer = [result[0] for result in sort_dic]
    return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
answer = solution(N, stages)
print(answer)