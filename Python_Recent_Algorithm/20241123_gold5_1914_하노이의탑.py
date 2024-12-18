import sys
sys.stdin = open('input_1914.txt')
readl = sys.stdin.readlines

n = int(readl()) #3

def hanoi(n):
    k=1    
    for i in range(n):    
        k(n+1)=2*k(n)+1
        return k(n+1)

print(hanoi(3))
