import sys
sys.stdin = open('input_9506.txt')
readl = sys.stdin.readline

s = [] #1, 2, 3
while True:
    n = int(readl().rstrip()) #6
    if n == -1:
        break
    for i in range(n): #6, 6 % 1 = 6
        if n % i == 0 and i != n:
            s.append(i)
    print(s)            
    
        
    
    