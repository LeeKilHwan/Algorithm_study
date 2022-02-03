def solution(numbers, hand):
    answer = ""
    left = [1, 4, 7]  # 왼손으로만 눌러야하는 경우
    right = [3, 6, 9]  # 오른손으로만 눌러야 하는 경우
    cur_position = ["*", "#"]  # 현재 손가락의 위치를 나타내준다.

    # 키패드를 2차원 배열의 좌표로 가정하고 각 키패드마다 좌표값을 값으로 가지는 dictionary를 생성
    dic = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        "*": (3, 0), 0: (3, 1), "#": (3, 2)
    }

    for next_num in numbers:
        # 다음 누를 숫자가 1,4,7일 경우 왼손으로 누르고 현재 손가락의 위치를 누른 숫자로 변경
        if next_num in left:
            answer += "L"
            cur_position[0] = next_num

        # 다음 누를 숫자가 3,6,9일 경우 오른손으로 누르고 현재 손가락의 위치를 누른 숫자로 변경
        elif next_num in right:
            answer += "R"
            cur_position[1] = next_num

        # 다음 누를 숫자가 2,5,8,0일 경우 오른손과 왼손의 각 위치별 다음 누를 숫자의 거리를 좌표값으로 구하여 값이 더 작은 손으로 누른다.
        # (단, 거리가 같을 경우에는 왼손잡이는 왼손, 오른손 잡이는 오른손으로 누른다.)
        else:
            left_distance = abs(dic[cur_position[0]][0] - dic[next_num][0]) + abs(
                dic[cur_position[0]][1] - dic[next_num][1])
            right_distance = abs(dic[cur_position[1]][0] - dic[next_num][0]) + abs(
                dic[cur_position[1]][1] - dic[next_num][1])
            if left_distance == right_distance:
                if hand == "right":
                    answer += "R"
                    cur_position[1] = next_num
                else:
                    answer += "L"
                    cur_position[0] = next_num
            else:
                if left_distance < right_distance:
                    answer += "L"
                    cur_position[0] = next_num
                else:
                    answer += "R"
                    cur_position[1] = next_num
    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
answer = solution(numbers, hand)
print(answer)