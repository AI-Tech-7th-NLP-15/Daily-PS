def solution(s):
    dic={'0':'zero', '1':'one', '2':'two', '3': 'three', '4': 'four', '5': 'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}
    
    for key in dic:
        s=s.replace(dic[key], key)
    
    return int(s)

# replace 활용하면 더 쉽게 풀 수 있다..
# replace 예) 'oxoxoxoxox'.replace('ox', '', 1) : 1개만 바꿔줌
