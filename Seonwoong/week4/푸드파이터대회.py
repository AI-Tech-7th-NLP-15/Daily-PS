def solution(food):
    for i in range(1, len(food)):
        if food[i] % 2 != 0:
            food[i] -= 1

    tmp = ''
    num = 0
    for i in range(len(food)):
        tmp += str(num) * (food[i] // 2)
        num += 1

    answer = ''
    answer += (tmp + '0' + tmp[::-1])
    return answer
