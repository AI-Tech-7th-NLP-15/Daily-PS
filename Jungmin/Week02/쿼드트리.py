import sys
sys.setrecursionlimit(10**6)

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

def recursive(arr, cord, shred, res):
    start_y, end_y, start_x, end_x = cord[0], cord[1], cord[2], cord[3]

    tot = sum(sum(arr[i][start_x:end_x]) for i in range(start_y, end_y))

    if tot == 0:
        return res + "0"

    elif tot == shred**2:
        return res + "1"

    else:
        mid_y = (start_y + end_y) // 2
        mid_x = (start_x + end_x) // 2

        top_left = [start_y, mid_y, start_x, mid_x]
        top_right = [start_y, mid_y, mid_x, end_x]
        bot_left = [mid_y, end_y, start_x, mid_x]
        bot_right = [mid_y, end_y, mid_x, end_x]

        res += "("

        res = recursive(arr, top_left, shred//2, res)
        res = recursive(arr, top_right, shred//2, res)
        res = recursive(arr, bot_left, shred//2, res)
        res = recursive(arr, bot_right, shred//2, res)

        res += ")"
        return res

cord = [0, N, 0, N]
shred = N
res = recursive(arr, cord, shred, "")
print(res)