def solution(k, m, score):
    score.sort(key=lambda x: -x)
    tot = 0
    idx = 0

    while idx + m <= len(score):
        tot += score[idx+m-1] * m
        idx += m

    return tot

print(solution(3, 4, [1, 2, 3, 1, 2, 3, 1])) # 8
print(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2])) # 33