import sys
sys.stdin = open('input_2711.txt')
readl = sys.stdin.readline
# 4
# 4 MISSPELL
# 1 PROGRAMMING
# 7 CONTEST
# 3 BALLOON

n = int(readl()) #4
for _ in range(n): 
    x, line = readl().split()
    x = int(x)
    
    print(line[:x-1] + line[x:])
