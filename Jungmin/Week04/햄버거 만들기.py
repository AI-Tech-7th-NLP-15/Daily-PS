def solution(ingredient):
    answer = 0
    ingredient = ingredient[::-1]
    stack = []

    while ingredient:
        stack.append(ingredient.pop())

        if len(stack) >= 4:
            if stack[-1] == 1 and stack[-2] == 3 and stack[-3] == 2 and stack[-4] == 1:
                stack.pop()
                stack.pop()
                stack.pop()
                stack.pop()

                answer += 1

    return answer


print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))