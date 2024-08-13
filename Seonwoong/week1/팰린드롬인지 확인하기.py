# 소요시간 1분 내외

import sys
input=sys.stdin.readline

arr=input().strip()
print(1 if arr==arr[::-1] else 0)
