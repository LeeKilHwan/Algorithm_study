# 아이디어
#   - skill_trees에 담긴 문자열을 deque에 담하서 하나씩 꺼내 가능한 스킬트리인지 확인한다
#   - skill순서를 list형태로 만들어준다.
#   - skill_trees에서 꺼낸 스킬트리를 반복문을 통해 skill에 있는 스킬만 빈 리스트에 담아준다.
#   - 0 부터 담긴 리스트이 개수만큼 인덱스번호로 skill의 값과 같은지 비교한다
#   - 하나라도 다를경우 temp를 1로 만들어준다.
#   - temp가 1일경우 불가능한 스킬트리이므로 아무것도 하지않고 temp가 0일 경우 가능한 스킬트리이므로 answer에 +1을 해준다.
#   - answer를 반환해준다.


from collections import deque

def solution(skill, skill_trees):
    answer = 0
    skill_trees = deque(skill_trees)
    skill = [num for num in skill]

    while skill_trees:
        answer_list = []
        temp = 0
        cur_skill = skill_trees.popleft()
        for word in cur_skill:
            if word in skill:
                answer_list.append(word)
        for idx in range(len(answer_list) + 1):
            if skill[:idx] != answer_list[:idx]:
                temp = 1
        if temp == 0:
            answer += 1

    return answer

skill, skill_trees = "CBD" , ["BACDE", "CBADF", "AECB", "BDA"]
answer = solution(skill, skill_trees)
print(answer)