def solution(id_list, report, k):
    answer = []
    mapper_ed = {}
    mapper_er = {}

    report = list(set(report))

    for log in report:
        reporter, reported = log.split(' ')
        if reported not in mapper_ed:
            mapper_ed[reported] = [1, [reporter]]

        else:
            mapper_ed[reported][0] += 1
            mapper_ed[reported][1].append(reporter)

        if mapper_ed[reported][0] == k:
            for rep in mapper_ed[reported][1]:
                if rep not in mapper_er:
                    mapper_er[rep] = 1

                else:
                    mapper_er[rep] += 1

        elif mapper_ed[reported][0] > k:
            if reporter not in mapper_er:
                mapper_er[reporter] = 1

            else:
                mapper_er[reporter] += 1

    for id in id_list:
        answer.append(mapper_er[id]) if id in mapper_er else answer.append(0)

    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)) # [2, 1, 1, 0]
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3)) # [0, 0]