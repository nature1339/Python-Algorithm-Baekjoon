import sys
sys.stdin = open('input_2609.txt')
readl = sys.stdin.readline

n = int(input())

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b) # a%b가 0될때까지 계속

for _ in range(n):
    A, B = map(int, readl().split())
    G = gcd(A, B) #최대 공약수
    a = A // G
    b = B // G
    L = G * a * b #최소 공배수 
    print(L)
    