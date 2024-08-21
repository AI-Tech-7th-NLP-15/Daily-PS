answer=''

def check(x,y,n):
    global answer
    number = tree[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if number!= tree[i][j]:
                number=-1
                break

    if number==-1:
        answer+='('
        check(x,y,n//2)
        check(x,y+n//2, n//2)
        check(x+n//2, y, n//2)
        check(x+n//2, y+n//2, n//2)
        answer+=')'

    elif number==1:
        answer+='1'

    else: 
        answer+='0'


n=int(input())
tree=[list(map(int,input())) for _ in range(n)]
check(0,0,n)
print(answer)
