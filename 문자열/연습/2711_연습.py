import sys
sys.stdin = open('input_2711.txt')
readl = sys.stdin.readline

# 4
# 4 MISSPELL
# 1 PROGRAMMING
# 7 CONTEST
# 3 BALLOON
l = []
sun = [] #4
n = int(readl())
for i in range(n):
    line = readl().rstrip()  #4 MISSPELL
    for j in range(line):  #line = 4 MISSPELL        
        line[0] = sun    #4 -> S
    print(l)