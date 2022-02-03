def solution(id_list, report, k):
    answer = []  # 처리 메일을 받아야 하는 아이디를 담아주기위한 list
    id_dic = {}  # 유저별로 몇명이, 누가 신고했는지를 담아주기 위한 dictionary
    cnt_dic = {}  # 유저별로 처리 메일이 발송되어야 하는 횟수를 담아주기 위한 dictionary

    # 같은 사람을 신고할 경우 1번만 적용되므로 같은 사람을 신고한 중복값을 제거해준다.
    removed_report = list(set(report))

    # 갹 dictionary를 생성해준다.
    for i in id_list:
        id_dic[i] = []
        cnt_dic[i] = 0

    # 유저별로 누구에게 신고당했는지를 id_dic에 담아준다.
    for name in removed_report:
        a, b = name.split()
        id_dic[b].append(a)

    # 처리 메일을 받아야 하는 아이디를 중복을 허용하여 모두 담아준다.
    an = list(map(lambda x: id_dic[x], id_dic))
    for i in id_dic:
        if len(id_dic[i]) >= k:
            for j in range(len(id_dic[i])):
                answer.append(id_dic[i][j])

    # 처리 메일을 받아야 하는 아이디로 처리 메일을 받아야 하는 숫자를 증가시켜준다.
    for l in answer:
        cnt_dic[l] += 1
    return list(cnt_dic.values())

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

answer = solution(id_list, report,k)
print(answer)