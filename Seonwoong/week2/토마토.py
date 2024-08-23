import sys
from collections import deque

m,n= map(int, sys.stdin.readline().split())
graph=[list(map(int, input().split())) for _ in range(n)]
queue=deque([])

for j in range(n):
  for k in range(m):
    if graph[j][k]==1:
      queue.append([j,k])

dy = [1,-1,0,0]
dz = [0,0,1,-1]

def bfs():
  while queue:
    y,z=queue.popleft()
    for i in range(4):
      b,c=y+dy[i], z+dz[i] 
      if 0<=b<n and 0<=c<m and graph[b][c]==0:
        queue.append([b,c])
        graph[b][c]=graph[y][z]+1

bfs()
maxday=0

for j in range(n):
  for k in range(m):
    if graph[j][k]==0:
      print(-1)
      exit(0)
    maxday=max(maxday, graph[j][k])

print(maxday-1)
