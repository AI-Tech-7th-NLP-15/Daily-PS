def solution(s):
    dic={'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    
    answer=''
    
    for i in range(len(s)):
        if s[i].isdigit():
            answer+=s[i]
        
        else:
            if i+3<=len(s): 
                num1=s[i:i+3]
                if num1 in dic.keys():
                    answer+=dic[num1]
                    i+=2
                
            if i+4<=len(s):
                num2=s[i:i+4]
                if num2 in dic.keys():
                    answer+=dic[num2]
                    i+=3
                    
            if i+5<=len(s):
                num3=s[i:i+5]
                if num3 in dic.keys():
                    answer+=dic[num3]
                    i+=4
                
    return int(answer)
