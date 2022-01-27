# 각 명함의 가로 세로 크기를 반복문을 통해 비교하여 더 길이가 긴 쪽을 가로 후보의 리스트에 담아준다
# 더 작은 수는 세로 후보의 리스트에 담아준다.
# 가로 후보의 리스트의 최대값과 세로 후보의 리스트의 최대값을 곱한 수를 반환한다.

def solution(sizes):
    answer = 0
    max_w = []
    max_h = []

    for i in sizes:
        if i[0] > i[1]:
            max_w.append(i[0])
            max_h.append(i[1])
        else:
            max_w.append(i[1])
            max_h.append(i[0])
    answer = max(max_w) * max(max_h)

    return answer

par = [[60, 50], [30, 70], [60, 30], [80, 40]]
answer = solution(par)
print(answer)