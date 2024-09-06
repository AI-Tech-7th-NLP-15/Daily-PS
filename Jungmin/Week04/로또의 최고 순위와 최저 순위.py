def solution(lottos, win_nums):
    answer = []

    lottos.sort()
    win_nums.sort()

    zero_count = lottos.count(0)
    correct_count = 0

    for num in lottos:
        if num in win_nums:
            correct_count += 1

    answer.append(7 - (correct_count + zero_count) if correct_count + zero_count > 0 else 6)
    answer.append(7 - correct_count if correct_count > 0 else 6)

    return answer

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])) # [3, 5]
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25])) # [1, 6]
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35])) # [1, 1]