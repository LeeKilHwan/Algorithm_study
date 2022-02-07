# 아이디어
#   - 주어진 문자열 numbers를 itertools의 permutations를 이용해 만들수 있는 모든 숫자를 만든다.
#   - numbers로 만들어진 숫자들 중 0,1이 아닌 경우에만 새로운 리스트에 담아준다.
#   - 담긴 리스트를 반복문을 통해 약수의 개수를 각각 구해주고 소수인지 판단하여 소수일 경우에만 answer에 1더해 반환해준다.


from itertools import combinations, permutations
import math
def solution(numbers):
    answer = 0
    li_list = []

    for i in range(1, len(numbers) + 1):
        per_list = list(permutations(numbers, i))

        for j in per_list:
            re = ''
            for k in range(len(j)):
                re += str(j[k])
            if re in li_list:
                continue
            if int(re) > 1:
                li_list.append(re)
    li_list = list(set(list(map(lambda x: int(x), li_list))))

    for num in li_list:
        cnt = 0
        nn = int(math.sqrt(num))
        for div in range(1, nn + 1):
            if num % div == 0:
                cnt += 1
        if cnt == 1:
            answer += 1
    return answer

numbers = "011"
answer = solution(numbers)
print(answer)

# 처음 문제를 풀었을 때 몇개의 몇개의 테스트케이스에서 시간이 오래 걸리고 몇개의 테스트 케이스는 시간초과로 실패했다.
# 문제의 제한사항을 보면 numbers는 7자리까지 가능하다고 나와있다. 만들 수 있는 숫자가 1자리 부터 7자리까지 모두 있을 경우 소수를 찾는 for문에서 많은 시간이
# 걸린다는 것을 알았다. 이를 해결하기위해 for문의 범위를 구하려는 숫자의 제곱근까지로 설정하고 불필요한 작업을 줄이고 시간을 절감하여 성공 할 수 있었다.