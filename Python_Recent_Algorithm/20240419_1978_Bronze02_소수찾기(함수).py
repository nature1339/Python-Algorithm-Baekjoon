import sys
sys.stdin = open('input_1978.txt')
readl = sys.stdin.readline

n = int(readl())
arr = list(map(int, readl().split())) #[1 3 5 7 ] 
# 4
# 1 3 5 7

# def func1(a, b):
#     print(a, b)
    
# def func2(a, b):
#     return a+b

# func1(n, n)
# x = func2(n, n)
# print(x)

def isPrime(m):
    if m == 1:
        return False
    
    for i in range(2, m):
        if m % i == 0:
            return False
    return True

sosu = 0

for m in arr: #소수 1과 자기자신으로만 나눠지는수
    if isPrime(m): # 함수가 true이면
        sosu += 1        
print(sosu)    
