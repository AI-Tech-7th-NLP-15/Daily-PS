def solution(ingredient):
    temp = []
    cnt = 0
    
    for i in ingredient:
        temp.append(i)
        if temp[-4:] == [1, 2, 3, 1]:
            cnt += 1
            for n in range(4):
                temp.pop() 
    
    return cnt
