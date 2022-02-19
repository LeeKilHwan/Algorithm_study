# 아이디어
#   - 의상의 종류를 key값으로 가지고 의상의 이름들을 list형태로 값으로 가지는 dictionary를 만들어준다.
#   - 의상의 종류를 기준으로 가지고 있는 값들의 개수를 answer_list에 담아준다.
#   - 담긴 리스트의 요소들을 1씩 더해서 곱해 모든 경우의 수를 구해준다.
#   - 스파이가 가진 의상수는 1개 이상이므로 아무것도 입지 않는 경우를 빼준다. ( -1 해준다)
#   - 결과값을 반환해준다.


def solution(clothes):
    answer = 1
    cl_dic = {}
    for i in clothes:
        cl_dic[i[-1]] = []
    for j in clothes:
        cl_dic[j[-1]].append(j[0])

    answer_list = []
    for cnt in cl_dic:
        answer_list.append(len(cl_dic[cnt]))

    for num in answer_list:
        answer *= (num + 1)
    answer = answer - 1
    return answer

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
answer = solution(clothes)
print(answer)

# 문제를 풀면서 수학적인 요소가 필요하다는 생각에 주어진 테스트 케이스를 수학적인 계산을 하기 위한 형태로 바꾸는 작업는 쉬웠지만, 수식을 세우는 과정이 어려웠었다.