def solution(id_list, report, k):
    
    reported = {id: set() for id in id_list}
    
    
    for r in set(report): 
        reporter, reported_user = r.split()
        reported[reported_user].add(reporter)
    
    
    answer = {id: 0 for id in id_list}
    for reported_user, reporters in reported.items():
        if len(reporters) >= k:
            for reporter in reporters:
                answer[reporter] += 1
    
    return [answer[id] for id in id_list]
