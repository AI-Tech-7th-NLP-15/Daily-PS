n=int(input())

a=list(map(int, input().split()))
b=list(map(int, input().split()))
a=sorted(a, reverse=True)
b=sorted(b)

answer=0
for i in range(n):
    answer+=(a[i]*b[i])
print(answer)
