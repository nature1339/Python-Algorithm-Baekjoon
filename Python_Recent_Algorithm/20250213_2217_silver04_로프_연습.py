import sys

input = sys.readline.stdin


s = list(map(int,input().split())) #10,15


for i in s:
    if i > i+1:
        s.pop(i)
    else:
        sum+=i

print(sum)