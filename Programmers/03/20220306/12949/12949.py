def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        result_list = []
        for j in range(len(arr2[0])):
            result = 0
            for k in range(len(arr1[0])):
                st = arr1[i][k]
                sc = arr2[k][j]
                result += st * sc
            result_list.append(result)
        answer.append(result_list)
    return answer

arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]
answer = solution(arr1,arr2)
print(answer)