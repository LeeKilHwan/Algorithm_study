def solution(s):
    answer = 1001
    l = len(s)
    anw = ""

    for cut_num in range(1, l // 2 + 1):
        string = ""

        for i in range(0, l, cut_num):
            if i == 0:
                unit = s[i:i + cut_num]
                cnt = 1
            else:
                if unit == s[i:i + cut_num]:
                    cnt += 1
                else:
                    if cnt > 1:
                        string += str(cnt) + unit
                    else:
                        string += unit
                    unit = s[i:i + cut_num]
                    cnt = 1

            if i + cut_num >= len(s):
                if cnt > 1:
                    string += str(cnt)
                string += unit

        if len(string) < answer:
            answer = len(string)

    if answer == 1001:
        answer = len(s)

    return answer

s = "aabbaccc"
answer = solution(s)
print(answer)