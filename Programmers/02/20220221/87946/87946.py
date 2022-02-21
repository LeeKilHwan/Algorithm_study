# 아이디어
#   - 순열을 이용하여 던전을 클리어하는 모든 순서를 만들어준다.
#   - 만들어진 순서를 반복문을 통해 피로도를 모두 사용할 때 까지 얼만큼 던전을 클리어할 수 있는지 카운트하여 빈 리스트에 담아준다.
#   - 리스트의 최대값이 던전을 가장 많이 클리어할 수 있는 경우의 수이므로 리스트의 최대값을 반환해준다.

from itertools import permutations
def solution(k, dungeons):
    answer = 0
    clear_list = list(permutations(dungeons, len(dungeons)))
    answer_list = []
    for order in clear_list:
        cnt = 0
        rest = k
        for require, use in order:
            if require <= rest:
                rest -= use
                cnt += 1
            else:
                break
        answer_list.append(cnt)
    answer = max(answer_list)
    return answer

k = 80
dungeons = [[80,20],[50,40],[30,10]]
answer = solution(k, dungeons)
print(answer)

# 처음에는 순열을 생각하지 못하여 필요한피로도와 사용되는피로도를 가지고 최적의 던전 클리어 순서를 만들어 풀이하였다.
# 4개의 테스트 케이스에서 실패가 발생했다.
# 결국 반례를 찾지 못하여 새로운 풀이가 잘못되었다고 생각하여 다른 풀이를 찾던 중 던전의 개수가 8개로 제한되어 있어 순열을 사용하여 풀이에 성공하였다.
# 앞선 풀이의 반례를 찾지 못하여 잘못된 풀이라고 생각하였지만 이와 같은 풀이로 푼 코드를 발견하였고 수학적 지식의 부족함을 느끼게 되었다.

# <이전 풀이방법>
#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# def solution(k, dungeons):
#     answer = 0
#     required = sorted(dungeons, key=lambda x: x[0], reverse=True)
#     use = sorted(dungeons, key=lambda x: x[1])
#
#     answer_list = []
#     for i in dungeons:
#         answer_list.append(required.index(i) + use.index(i))
#     print(answer_list)
#
#     clear_list = []
#     while min(answer_list) < 5000:
#         a = answer_list.index(min(answer_list))
#         clear_list.append(dungeons[a])
#         answer_list[a] = 5000
#     for n in clear_list:
#         if n[0] <= k and n[1] <= k:
#             k -= n[1]
#             answer += 1
#     return answer
#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# dungeons = sorted(dungeons, key = lambda x : ((x[1]+x[0])/x[0],x[1])) 로 구하면 던전의 최적의 클리어 순서를 구할 수 있었다.