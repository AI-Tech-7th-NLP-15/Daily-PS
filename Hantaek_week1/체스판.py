def count_repaints(board, start_row, start_col, pattern):
    count = 0
    for i in range(8):
        for j in range(8):
            if board[start_row + i][start_col + j] != pattern[i][j]:
                count += 1
    return count

def get_minimum_repaints(board, N, M):
    pattern1 = [['B', 'W'] * 4, ['W', 'B'] * 4] * 4
    pattern2 = [['W', 'B'] * 4, ['B', 'W'] * 4] * 4
    
    min_repaints = float('inf')
    
    for i in range(N - 7):
        for j in range(M - 7):
            repaints_pattern1 = count_repaints(board, i, j, pattern1)
            repaints_pattern2 = count_repaints(board, i, j, pattern2)
            min_repaints = min(min_repaints, repaints_pattern1, repaints_pattern2)
    
    return min_repaints


N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]


result = get_minimum_repaints(board, N, M)


print(result)
