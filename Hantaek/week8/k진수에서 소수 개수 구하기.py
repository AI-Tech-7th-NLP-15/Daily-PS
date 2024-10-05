def solution(n, k):
    answer = 0
    
    def ten_n(a, b):
        rev_dev = ''
        while a > 0:
            a, q = divmod(a, b)
            rev_dev += str(q)
        return rev_dev[::-1]
    
    def sosu(num):
        if num == 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    result = ten_n(n, k)
    result_list = result.split('0')
    
    for l in result_list:
        if l and sosu(int(l)):
            answer += 1
    
    return answer