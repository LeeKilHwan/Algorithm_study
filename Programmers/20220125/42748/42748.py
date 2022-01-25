def solution(array, commands):
    answer = []
    for i in commands:
        result_list = []

        result_list = array[i[0] - 1: i[1]]
        result_list.sort()

        answer.append(result_list[i[2] - 1])
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
answer = solution(array, commands)
print(answer)