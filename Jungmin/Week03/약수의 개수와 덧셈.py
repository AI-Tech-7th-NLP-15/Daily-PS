def solution(left, right):
    arr = [0] * 1001
    answer = 0

    for i in range(1, 1001):
        for j in range(i, 1001, i):
            arr[j] += 1

    for i in range(left, right + 1):
        if arr[i] % 2 == 0:
            answer += i
        else:
            answer -= i

    return answer