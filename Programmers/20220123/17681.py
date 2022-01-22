# 1.배열안의 숫자를 이진수로 변경해준다.
# 2.배열1과 배열2를 비교하면서 하나라도 벽인 부분은 벽, 벽이 아닌 부분을 공백으로 반환하여 새로운배열로
#  만들어준다.
def solution(n, arr1, arr2):
    answer = []

    cnt1 = 0
    cnt2 = 0
    # 배열안의 숫자를 사각형 길이만큼의 이진수로 바꾸어준다.

    for i in arr1:
        result = ''
        while i > 0:
            result += str(i % 2)
            i = i // 2
        result = result[::-1]
        if len(result) < n:
            result = '0' * (n - len(result)) + result
        arr1[cnt1] = result
        cnt1 += 1
    for i in arr2:
        result = ''
        while i > 0:
            result += str(i % 2)
            i = i // 2
        result = result[::-1]
        if len(result) < n:
            result = '0' * (n - len(result)) + result
        arr2[cnt2] = result
        cnt2 += 1

    # 변환해준 배열1과 배열2를 비교하여 둘다 0인 경우에만 공백, 하나라도 1일경우 #으로
    # result2에 순서대로 문자열을 더해준뒤 완성된 문자열은 answer리스트에 담아준다.
    for i in range(n):
        result2 = ""
        for j in range(n):
            if arr1[i][j] == "0" and arr2[i][j] == "0":
                result2 += " "
            else:
                result2 += "#"
        answer.append(result2)
    return answer

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
answer = solution(n, arr1, arr2)
print(answer)