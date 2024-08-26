def solution(survey, choices):
    answer = ''
    dic={'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    
    for i in range(len(survey)):
        if choices[i]<4: dic[survey[i][0]]+=4-choices[i]
        elif choices[i]>4: dic[survey[i][1]]+=choices[i]-4  
    
    print(dic)
    
    if dic['R']>=dic['T']: answer+='R'
    else: answer+='T'
    
    if dic['C']>=dic['F']: answer+='C'
    else: answer+='F'

    if dic['J']>=dic['M']: answer+='J'
    else: answer+='M'
    
    if dic['A']>=dic['N']: answer+='A'
    else: answer+='N'
    
    return answer
