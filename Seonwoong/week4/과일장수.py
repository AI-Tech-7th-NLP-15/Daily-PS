def solution(k, m, score):
    answer = 0
    
    score.sort(reverse=True)
    i = 0
    while (i + m <= len(score)):
        box = score[i : i + m]
        price = min(box) * len(box)
        answer += price
        
        i += m
        
    return answer
