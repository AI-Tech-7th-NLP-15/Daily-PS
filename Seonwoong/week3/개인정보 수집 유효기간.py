def solution(today, terms, privacies):
    answer = []
    
    today=int(today[0:4])*12*28+int(today[5:7])*28+int(today[8:10])
    for i in range(len(privacies)):
        grade=privacies[i][-1]
        privacies[i]=int(privacies[i][0:4])*12*28+int(privacies[i][5:7])*28+int(privacies[i][8:10])
        
        for j in range(len(terms)):
            if grade==terms[j][0]:
                privacies[i]+=28*int(terms[j][2:])
                
        if privacies[i]<=today: 
            answer.append(i+1)
    
    return answer
