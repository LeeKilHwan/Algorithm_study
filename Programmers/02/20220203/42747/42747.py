# 아이디어
#   - 주어진 배열 citations를 오름차순 정려해준다.
#   - 정렬된 배열의 -1부터 for문을 돌리기 위해 범위를 1 부터 배열의 개수만큼으로 설정한다.
#   - for문의 인덱스보다 citaions[인덱스]가 크거나 같은 최대값을 반환해준다.
#   - (for문의 인덱스는 인덱스를 나태님과 동시에 citations[인덱스]를 인용한 논문의 숫자를 의미함)
def solution(citations):
    answer = 0
    citations.sort()

    for num in range(1, len(citations) + 1):
        if num <= citations[-num]:
            answer = num
    print(citations)
    return answer

citations = [3, 0, 6, 1, 5]
answer = solution(citations)
print(answer)