import sys
input=sys.stdin.readline

arr=input().strip()
print(1 if arr==arr[::-1] else 0)
