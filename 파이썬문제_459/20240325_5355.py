import sys
sys.stdin = open('input_5355.txt')
readl = sys.stdin.readline

n = int(readl()) #3
line = readl().split() # '3','@', '%'


x == '@': # *3
y == '%': # + 5
z == '#': # -7
result = 1
    
for i in range(n): #3
    for j in line: # '3','@', '%'    3*3+5
       result *= line[j]  #3*3+5  j[i]j[i+1]j[i+2]
    
   