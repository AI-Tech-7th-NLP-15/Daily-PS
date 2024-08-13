# 소요시간 7분 내외

import sys
input=sys.stdin.readline

n, m=map(int, input().split())
data=[list(input().strip()) for _ in range(n)]
answer=[]

for i in range(0,n-7):
    for j in range(0,m-7):

        #cnt1, cnt2 : WBW.. BWB.. 카운트 변수
        cnt1,cnt2=0,0

        for x in range(i,i+8):
            for y in range(j,j+8):
                if (x+y)%2==0:
                    if data[x][y]!='W': cnt1+=1
                    if data[x][y]!='B': cnt2+=1
                else:
                    if data[x][y]!='B': cnt1+=1
                    if data[x][y]!='W': cnt2+=1

        if cnt1>cnt2: answer.append(cnt2)
        else: answer.append(cnt1)

print(min(answer))
