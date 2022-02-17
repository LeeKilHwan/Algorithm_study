# 아이디어
#   - 탈락자가 발생하지 않는 경우 [0,0]을 반환
#   - 탈락자가 발생하는 경우 [탈락한 플레이어, 탈락한 라운드]를 반환해준다.
#   - 주어진 배열을 deque에 담아 사용한단어 used_list에 담아준다.
#   - 첫글자가 맞지 않거나 이미 사용되었던 단어가 나오는 경우 탈락
#   - 탈락이 발생했을때 [플레이어,스테이지]를 answer로 반환해주고 break로 반복문을 종료해준다.

from collections import deque
def solution(n, words):
    answer = [0,0]
    words = deque(words)
    used_list = []
    stage, player = 1,0
    while words:
        if player == n:
            stage += 1
            player = 1
        else:
            player += 1
        cur_word = words.popleft()
        if len(used_list) == 0:
            used_list.append(cur_word)
        else:
            if used_list[-1][-1] == cur_word[0] and cur_word not in used_list:
                used_list.append(cur_word)
            else:
                answer = [player, stage]
                break
    return answer

n, words = 3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
answer = solution(n, words)
print(answer)