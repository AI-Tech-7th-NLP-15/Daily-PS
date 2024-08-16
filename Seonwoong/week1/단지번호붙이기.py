import sys
input = sys.stdin.readline
from collections import deque

n=int(input())
graph=[list(map(int, input().strip())) for _ in range(n)]
answer=[]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    queue=deque()
    queue.append([x,y])
    graph[x][y]=0
    cnt=1

    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx, ny= x+dx[i], y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n or graph[nx][ny]==0:
                continue

            if graph[nx][ny]==1:
                graph[nx][ny]=0
                queue.append([nx,ny])
                cnt+=1

    return cnt

for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            answer.append(bfs(i,j))

print(len(answer))
answer.sort()
for i in answer:
    print(i)
