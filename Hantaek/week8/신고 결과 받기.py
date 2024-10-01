def solution(id_list, report, k):
    
    reported = {id: set() for id in id_list}
    
    
    for r in set(report):  # 중복 신고 제거
        reporter, reported_user = r.split()
        reported[reported_user].add(reporter)
    
    # 메일 수신 횟수 계산
    answer = {id: 0 for id in id_list}
    for reported_user, reporters in reported.items():
        if len(reporters) >= k:  # k번 이상 신고된 경우
            for reporter in reporters:
                answer[reporter] += 1
    
    return [answer[id] for id in id_list]