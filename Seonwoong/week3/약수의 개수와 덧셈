def cnt(n):
    count=0
    for i in range(1, (int)(n**(1/2))+1):
        if i*i==n: count+=1
        elif n%i==0: count+=2   
    return count

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if cnt(i)%2==0:
            answer+=i
        else:
            answer-=i

    return answer
