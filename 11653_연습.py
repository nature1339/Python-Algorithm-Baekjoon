import sys
sys.stdin = open('input_11653.txt')
readl = sys.stdin.readline

n = int(readl())
l = []


for i in range(n): #72
    if n % 2 == 0: #n이 2로 나누어 떨어지면, 계속반복
        l.append[i]
       n = n // 2  
    if n % 3 == 0: #n이 3으로 나누어떨어지면,.. 소수일때만나눔   
       