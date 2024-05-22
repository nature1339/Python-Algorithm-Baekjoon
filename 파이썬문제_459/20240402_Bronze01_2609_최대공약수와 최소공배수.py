import sys
sys.stdin = open('input_2609.txt')
readl = sys.stdin.readline


A, B = map(int, readl().split())  #24 18

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

G = gcd(A,B) # 최대공약수
m = A // G
n = B // G
L = G * m * n # 최소공배수
print(G)
print(L)  
    
    

    