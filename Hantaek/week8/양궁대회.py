from itertools import combinations_with_replacement

def solution(n, info):
    max_diff = 0
    best_comb = [-1]

    for comb in combinations_with_replacement(range(11), n):
        ryan_info = [0] * 11
        for i in comb:
            ryan_info[10 - i] += 1

        ryan_score, apeach_score = 0, 0
        for i in range(11):
            if info[i] == 0 and ryan_info[i] == 0:
                continue
            if ryan_info[i] > info[i]:
                ryan_score += 10 - i
            else:
                apeach_score += 10 - i

        diff = ryan_score - apeach_score
        if diff > max_diff:
            max_diff = diff
            best_comb = ryan_info

    return best_comb