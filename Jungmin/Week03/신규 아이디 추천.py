def solution(new_id):
    new_id = new_id.lower()

    for elem in new_id:
        if (not 'a' <= elem <= 'z') and (not '0' <= elem <= '9') and elem != '-' and elem != '_' and elem != '.':
            new_id = new_id.replace(elem, '')

    for i in range(15, 1, -1):
        fix = '.' * i
        new_id = new_id.replace(fix, '.')

    if new_id and new_id[0] == '.':
        new_id = new_id[1:]

    if new_id and new_id[-1] == '.':
        new_id = new_id[:-1]

    if not new_id:
        new_id = "a"

    if len(new_id) >= 16:
        new_id = new_id[:15]

        if new_id[-1] == '.':
            new_id = new_id[:-1]

    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]

    return new_id

print(solution("...!@BaT#*..y.abcdefghijklm")) # "bat.y.abcdefghi"
print(solution("z-+.^.")) # "bat.y.abcdefghi"
print(solution("=.=")) # "bat.y.abcdefghi"
print(solution("123_.def")) # "bat.y.abcdefghi"
print(solution("abcdefghijklmn.p")) # "bat.y.abcdefghi"