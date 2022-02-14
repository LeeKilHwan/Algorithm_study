# 아이디어
#   - 주어진 문자열 phone_book을 정렬한다.
#   - 문자열은 숫자의 아스키 코드 값순서로 정렬되기 때문에 정렬된 리스트를 순서대로 2개씩 비교하여 접두어로 쓰였는지를 판단해준다.

def solution(phone_book):
    answer = True
    phone_book.sort()

    for idx in range(len(phone_book) - 1):
        if phone_book[idx] == phone_book[idx + 1][:len(phone_book[idx])]:
            answer = False

    return answer

phone_book = ["119", "97674223", "1195524421"]
answer = solution(phone_book)
print(answer)


# <처음 풀었던 풀이>
# def solution(phone_book):
#     answer = True
#     phone_book = sorted(phone_book,key = lambda x: len(x), reverse = True)
#     while phone_book:
#         ph = phone_book.pop()
#         for idx in phone_book:
#             if ph == idx[:len(ph)]:
#                 answer = False
#     return answer

# 이 방법으로 풀었을 경우 문자의 제한길이 1 이상 1,000,000 이하의 상황에서 while문안에 for문을 돌리면
# 시간 복잡도가 초과하여 효율성 테스트를 통과하지 못했다. 이를 해결하기위해 for문을 한번만 돌리는 방향으로 문제를 해결하였다.