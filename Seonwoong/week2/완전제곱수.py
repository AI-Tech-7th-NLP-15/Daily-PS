square=[i*i for i in range(1,101)]

m=int(input())
n=int(input())

cnt,total,minV=0,0,10000

for i in range(m,n+1):
    if i in square:
        cnt+=1
        total+=i
        minV=min(minV, i)

if cnt==0: 
    print(-1)
else:
    print(total)
    print(minV)
