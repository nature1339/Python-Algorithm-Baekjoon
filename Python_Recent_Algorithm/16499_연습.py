import sys
sys.stdin = open('input_16499.txt')
readl = sys.stdin.readline

n = int(readl())

# sg = set(readl() for i in range())

sg = []

# cat
# dog
# god
# tca

sg = set()#(c,a,t) [] 
cnt = 0

for i in range(n):
    num = set(readl()) #cat 문자열 집합 cat  tac
    if num in sg:
        cnt += 1    
print(cnt)    
