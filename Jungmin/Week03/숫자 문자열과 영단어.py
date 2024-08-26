def solution(s):
    map = {
        "zero" : 0,
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9
    }

    for elem in map:
        s = s.replace(elem, str(map[elem]))

    return int(s)

test = ["one4seveneight", "23four5six7", "2three45sixseven", "123"]
for elem in test:
    print(solution(elem))